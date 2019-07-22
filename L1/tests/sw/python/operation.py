 # Copyright 2019 Xilinx, Inc.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.

import numpy as np
import sys
import pdb

t_Debug= True

class DataGenerator:
  def __init__(self, engine = np.random.random):
    self.engine = engine

  def setRange(self, minValue, maxValue):
    self.minValue = minValue
    self.maxValue = maxValue

  def setDataType(self, dtype):
    self.dataType = dtype

  def data(self, size:tuple):
    v = self.engine(size) * (self.maxValue - self.minValue) + self.minValue
    v = v.astype(self.dataType)
    return v

  def scalar(self, value=None):
    tup = (1)
    v = self.data(tup)
    if value:
      v[0] = value
    return v

  def vector(self, size:int):
    tup = (size)
    return self.data(tup)

  def matrix(self, size:tuple):
    assert len(size) == 2
    return self.data(size)

  def symmetricMatrix(self, size:int):
    tup = (size, size)
    mat = self.matrix(tup)
    mat = (mat + mat.transpose())/2
    return mat.astype(self.dataType) 

  def symmetricBandedMatrix(self, size:int, k:int):
    tupS = (size, size)
    tupK = (k, k)
    mat = self.bandedMatrix(tupS, tupK)
    mat = (mat + mat.transpose())/2
    return mat.astype(self.dataType) 

  def bandedMatrix(self, size:tuple, k:tuple):
    assert len(size) == 2
    assert len(k) == 2
    m, n = size
    kl, ku = k
    matrix = self.matrix(size)
    for i in range(m):
      for j in range(n):
        if i - j > kl or i - j < -ku:
          matrix[i][j] = 0
    return matrix

  def bandedMatrixStorage(self, matrix, k, colAlign=True):
    assert len(matrix.shape) == 2
    m, n = matrix.shape
    assert len(k) == 2
    kl, ku = k
    if colAlign:
      aDim = m +ku if m < n else n
      a = np.zeros((kl+ku+1, aDim), dtype=self.dataType)
      for i in range(-kl, ku+1):
        v = np.diag(matrix, i)
        startIndex = 0 if i < 0 else i
        a[ku - i][startIndex:startIndex+len(v)] = v
    else:
      pass
    return a

def dataGen(dataType, size, maxValue, minValue):
  a = np.random.random(size) * (maxValue - minValue) + minValue
  a = a.astype(dataType)
  return a


class OP_ERROR(Exception):
  def __init__(self, message):
    self.message = message
class OP:
  opDict = {
    'BLAS_L1': ('amax', 'amin', 'asum', 'axpy', 'swap', 'scal', 'dot', 'copy', 'nrm2'),
    'BLAS_L2': ('gemv', 'gbmv', 'sbmv', 'symv')
  }
  @staticmethod
  def parse(opName):
    for cls, ops in OP.opDict.items():
      if opName in ops:
        return cls
    raise OP_ERROR("opName %s is not supported."%opName)

  def __init__(self):
    pass

  def setDtype(self, dataType):
    self.dataType = dataType


class BLAS_L1(OP):
  @staticmethod
  def parse(opName, maxV, minV):
    try:
      op= eval(opName)(BLAS_L1(opName, maxV, minV))
      return op
    except:
      raise OP_ERROR("%s is not defined."%opName)
  def __init__(self, name, maxV, minV):
    self.name = name
    self.maxV = maxV
    self.minV = minV
    self.interfaceList=('p_x', 'p_y', 'p_xRes', 'p_yRes')
  def copyConstructor(self, object):
    self.name = object.name
    self.maxV = object.maxV
    self.minV = object.minV
    self.interfaceList= object.interfaceList
  def setRtype(self, rtype):
    self.rtype = rtype
  def setSize(self, size):
    self.vectorDim = size
    self.sizeStr = "v%d"%size

  def compute(self): 
    self.dataGen = DataGenerator()
    self.dataGen.setRange(self.minV, self.maxV)
    self.dataGen.setDataType(self.dataType)
    x = y = xr = yr = None
    alpha = self.dataGen.scalar()
    r = self.dataGen.scalar(0)
    return alpha, x, y, xr, yr, r
  def addInstr(self, blas_gen, register):
    for alpha, x, y, xr, yr, r in register:
      blas_gen.addB1Instr(self.name, self.vectorDim, alpha, x, y, xr, yr, r.astype(self.rtype))


  def test(self, runTest):
    vecDimList = runTest.profile['vectorDims']
    dataTypeList = runTest.dataTypes
    retTypeList = runTest.retTypes
    for dataType, retType in zip(dataTypeList, retTypeList):
      self.setDtype(dataType)
      self.setRtype(retType)
      for vecDim in vecDimList:
        self.setSize(vecDim)
        runTest.run()

  def paramTCL(self, f):
    f.write('   L1 true\n ')
    f.write('   opName "%s"\n '%self.name)
    f.write('   vectorSize %d\n '%self.vectorDim)

class amin(BLAS_L1):
  def __init__(self, blas_l1: BLAS_L1):
    self.copyConstructor(blas_l1)

  def compute(self): 
    alpha, x, y, xr, yr, r = BLAS_L1.compute(self)
    x = self.dataGen.vector(self.vectorDim)
    r = np.argmin(np.abs(x))
    return alpha, x, y, xr, yr, r


class amax(BLAS_L1):
  def __init__(self, blas_l1: BLAS_L1):
    self.copyConstructor(blas_l1)

  def compute(self): 
    alpha, x, y, xr, yr, r = BLAS_L1.compute(self)
    x = self.dataGen.vector(self.vectorDim)
    r = np.argmax(np.abs(x))
    return alpha, x, y, xr, yr, r

class asum(BLAS_L1):
  def __init__(self, blas_l1: BLAS_L1):
    self.copyConstructor(blas_l1)

  def compute(self): 
    alpha, x, y, xr, yr, r = BLAS_L1.compute(self)
    x = self.dataGen.vector(self.vectorDim)
    r = np.sum(np.abs(x))
    return alpha, x, y, xr, yr, r

class axpy(BLAS_L1):
  def __init__(self, blas_l1: BLAS_L1):
    self.copyConstructor(blas_l1)

  def compute(self): 
    alpha, x, y, xr, yr, r = BLAS_L1.compute(self)
    x = self.dataGen.vector(self.vectorDim)
    y = self.dataGen.vector(self.vectorDim)
    yr = alpha * x+ y
    return alpha, x, y, xr, yr, r

class copy(BLAS_L1):
  def __init__(self, blas_l1: BLAS_L1):
    self.copyConstructor(blas_l1)

  def compute(self): 
    alpha, x, y, xr, yr, r = BLAS_L1.compute(self)
    yr = x = self.dataGen.vector(self.vectorDim)
    return alpha, x, y, xr, yr, r

class dot(BLAS_L1):
  def __init__(self, blas_l1: BLAS_L1):
    self.copyConstructor(blas_l1)

  def compute(self): 
    alpha, x, y, xr, yr, r = BLAS_L1.compute(self)
    x = self.dataGen.vector(self.vectorDim)
    y = self.dataGen.vector(self.vectorDim)
    r=np.dot(x, y)
    return alpha, x, y, xr, yr, r

class nrm2(BLAS_L1):
  def __init__(self, blas_l1: BLAS_L1):
    self.copyConstructor(blas_l1)

  def compute(self): 
    alpha, x, y, xr, yr, r = BLAS_L1.compute(self)
    x = self.dataGen.vector(self.vectorDim)
    r = np.linalg.norm(x)
    return alpha, x, y, xr, yr, r

class swap(BLAS_L1):
  def __init__(self, blas_l1: BLAS_L1):
    self.copyConstructor(blas_l1)

  def compute(self): 
    alpha, x, y, xr, yr, r = BLAS_L1.compute(self)
    yr = x = self.dataGen.vector(self.vectorDim)
    xr = y = self.dataGen.vector(self.vectorDim)
    return alpha, x, y, xr, yr, r

class scal(BLAS_L1):
  def __init__(self, blas_l1: BLAS_L1):
    self.copyConstructor(blas_l1)

  def compute(self): 
    alpha, x, y, xr, yr, r = BLAS_L1.compute(self)
    x = self.dataGen.vector(self.vectorDim)
    xr = alpha * x
    return alpha, x, y, xr, yr, r


class BLAS_L2(OP):
  @staticmethod
  def parse(opName, maxV, minV):
    try:
      op = eval(opName)(BLAS_L2(opName, maxV, minV))
      return op
    except:
      raise OP_ERROR("%s is not defined."%opName)

  def __init__(self, name, maxV, minV):
    self.name=name
    self.maxV = maxV
    self.minV = minV
    self.interfaceList=('p_a', 'p_x', 'p_y', 'p_aRes', 'p_yRes')

  def copyConstructor(self, object):
    self.name = object.name
    self.maxV = object.maxV
    self.minV = object.minV
    self.interfaceList= object.interfaceList

  def compute(self): 
    self.dataGen = DataGenerator()
    self.dataGen.setRange(self.minV, self.maxV)
    self.dataGen.setDataType(self.dataType)
    a = x = y = ar = yr = None
    alpha = self.dataGen.scalar()
    beta = self.dataGen.scalar()
    return alpha, beta, a, x, y, ar, yr

  def addInstr(self, blas_gen, register):
    for alpha, beta, a, x, y, ar, yr in register:
      blas_gen.addB2Instr(self.name, self.m, self.n, self.kl, self.ku, 
        alpha, beta, a, x, y, ar, yr)

  def setSize(self, mn):
    self.matrixDim = tuple(mn)
    self.m = mn[0]
    self.n = mn[1]
    self.sizeStr = "m%d-n%d"%(self.m,self.n)

  def paramTCL(self, f):
    f.write('   L2 true\n ')
    f.write('   opName "%s"\n '%self.name)
    f.write('   matrixSize %d\n '%(self.m * self.n))
    f.write('   vectorSize %d\n '%self.n)

  def test(self, runTest):
    vecDimList = runTest.profile['matrixDims']
    dataTypeList = runTest.dataTypes
    for dataType in dataTypeList:
      self.setDtype(dataType)
      for vecDim in vecDimList:
        self.setSize(vecDim)
        runTest.run()

  def testBand(self, runTest):
    matrixDimList = runTest.profile['matrixDims']
    dataTypeList = runTest.dataTypes
    kulList = runTest.profile['kulList']
    for dataType in dataTypeList:
      self.setDtype(dataType)
      for kul in kulList:
        self.setK(kul)
        for matrixDim in matrixDimList:
          self.setSize(matrixDim)
          runTest.run()

class gemv(BLAS_L2):
  def __init__(self, blas_l2: BLAS_L2):
    self.copyConstructor(blas_l2)
  def compute(self):
    alpha, beta, a, x, y, ar, yr = BLAS_L2.compute(self)
    matrix = self.dataGen.matrix(self.matrixDim)
    x = self.dataGen.vector(self.n)
    y = self.dataGen.vector(self.m)
    yr = alpha * np.matmul(matrix, x) + beta * y
    return alpha, beta, matrix, x, y, ar, yr

class gbmv(BLAS_L2):
  def __init__(self, blas_l2: BLAS_L2):
    self.copyConstructor(blas_l2)

  def setK(self, kul):
    self.k=tuple(kul)
    self.ku = kul[0]
    self.kl = kul[1]
    self.sizeStr = "m%d-n%d-u%d-l%d"%(self.m,self.n,self.ku,self.kl)
    if self.ku < self.n - self.m:
      print("WARNING: Current matrix configuration has multiple zero columns")
    if self.m - self.n > self.kl:
      print("WARNING: Current matrix configuration has multiple zero rows")

  def compute(self):
    alpha, beta, a, x, y, ar, yr = BLAS_L2.compute(self)
    a, matrix = self.bandMatrix()
    matrix = self.dataGen.bandedMatrix(self.matrixDim, self.k)
    a = self.dataGen.bandedMatrixStorage(matrix, self.k)
    x = self.dataGen.vector(self.n)
    y = self.dataGen.vector(self.m)
    yr = alpha * np.matmul(matrix, x) + beta * y
    t_Debug and print("Matrix:\n", matrix)
    t_Debug and print("Storage:\n",a)
    return alpha, beta, a, x, y, ar, yr

  def bandMatrix(self):
    matrix = dataGen(self.dataType, self.matrixDim, self.maxV, self.minV)
    aDim = self.m +self.ku if self.m < self.n else self.n
    a = np.zeros((self.kl+self.ku+1, aDim), dtype=self.dataType)
    for i in range(-self.kl, self.ku+1):
      v = np.diag(matrix, i)
      startIndex = 0 if i < 0 else i
      a[self.ku - i][startIndex:startIndex+len(v)] = v
    for i in range(self.m):
      for j in range(self.n):
        if i - j > self.kl or i - j < -self.ku:
          matrix[i][j] = 0
    return a, matrix

  def test(self, runTest):
    self.testBand(runTest)


class symv(BLAS_L2):
  def __init__(self, blas_l2: BLAS_L2):
    self.copyConstructor(blas_l2)

  def setSize(self, m):
    self.matrixDim =(m ,m) 
    self.m = m
    self.n = m
    self.sizeStr = "m%d"%(self.m)

  def compute(self):
    alpha, beta, a, x, y, ar, yr = BLAS_L2.compute(self)
    matrix = self.dataGen.matrix(self.matrixDim)
    matrix = matrix + np.transpose(matrix)
    x = self.dataGen.vector(self.n)
    y = self.dataGen.vector(self.m)
    yr = alpha * np.matmul(matrix, x) + beta * y
    return alpha, beta, matrix, x, y, ar, yr

class sbmv(BLAS_L2):
  def __init__(self, blas_l2: BLAS_L2):
    self.copyConstructor(blas_l2)

  def setK(self, k):
    self.k = k
    self.sizeStr = "m%d_k%d"%(self.m, k)

  def setSize(self, m):
    self.matrixDim =(m ,m) 
    self.m = m
    self.n = m

  def compute(self):
    alpha, beta, a, x, y, ar, yr = BLAS_L2.compute(self)
    a = np.zeros((self.k*2+1, self.m), dtype=self.dataType)
    v = dataGen(self.dataType, self.m, self.maxV, self.minV)
    a[self.k][:] = v
    band_mat = np.diag(v)
    for i in range(1, self.k+1):
      v = dataGen(self.dataType, self.m - i, self.maxV, self.minV)
      a[self.k + i][:len(v)] = v
      a[self.k - i][self.m-len(v):] = v
      band_mat = band_mat + np.diag(v, i)
      band_mat = band_mat + np.diag(v, -i)
    x = self.dataGen.vector(self.n)
    y = self.dataGen.vector(self.m)
    yr = alpha * np.matmul(band_mat, x) + beta * y
    return alpha, beta, a, x, y, ar, yr

  def test(self, runTest):
    self.testBand(runTest)

def main():

  opName = 'gbmv'
  className = None
  for cls, ops in OP.opDict.items():
    if opName in ops:
      className = cls
      break

  if className:
    op  = eval(className).parse(opName, -24,   24)
    op.setDtype(np.int32)
    op.setSize([int(sys.argv[1]), int(sys.argv[2])])
    op.setK([int(sys.argv[3]), int(sys.argv[4])])
    alpha, beta, a, x, y, ar, yr = op.compute()

if __name__=='__main__':
  main()
