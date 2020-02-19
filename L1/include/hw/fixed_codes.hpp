#define STABLE_SIZE 544
const uint8_t fixed_litml_op[STABLE_SIZE] = {
    96, 0,  0,  20, 18, 0,  0,  0,  16, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  19, 0,  0,  0,  17, 0,  0,  0,  0,
    0,  0,  0,  16, 0,  0,  21, 19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  20, 0,  0,  0,  18, 0,
    0,  0,  0,  0,  0,  0,  16, 0,  0,  21, 19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  20, 0,  0,
    0,  18, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  64, 19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,
    20, 0,  0,  0,  18, 0,  0,  0,  0,  0,  0,  0,  96, 0,  0,  21, 18, 0,  0,  0,  16, 0,  0,  0,  0,  0,  0,  0,  16,
    0,  0,  0,  19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  16, 19, 0,  0,  0,  17, 0,  0,  0,  0,  0,
    0,  0,  16, 0,  0,  0,  20, 0,  0,  0,  18, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  21, 19, 0,  0,  0,  17, 0,  0,
    0,  0,  0,  0,  0,  16, 0,  0,  0,  20, 0,  0,  0,  18, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  64, 19, 0,  0,  0,
    17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  20, 0,  0,  0,  18, 0,  0,  0,  0,  0,  0,  0,  96, 0,  0,  20, 18,
    0,  0,  0,  16, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,
    0,  21, 19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  20, 0,  0,  0,  18, 0,  0,  0,  0,  0,  0,
    0,  16, 0,  0,  21, 19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  20, 0,  0,  0,  18, 0,  0,  0,
    0,  0,  0,  0,  16, 0,  0,  64, 19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  20, 0,  0,  0,  18,
    0,  0,  0,  0,  0,  0,  0,  96, 0,  0,  21, 18, 0,  0,  0,  16, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  0,  19, 0,
    0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  16, 19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,
    0,  20, 0,  0,  0,  18, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  21, 19, 0,  0,  0,  17, 0,  0,  0,  0,  0,  0,  0,
    16, 0,  0,  0,  20, 0,  0,  0,  18, 0,  0,  0,  0,  0,  0,  0,  16, 0,  0,  64, 19, 0,  0,  0,  17, 0,  0,  0,  0,
    0,  0,  0,  16, 0,  0,  0,  20, 0,  0,  0,  18, 0,  0,  0,  0,  0,  0,  0,  16, 23, 19, 27, 17, 25, 21, 29, 16, 24,
    20, 28, 18, 26, 22, 64, 16, 23, 19, 27, 17, 25, 21, 29, 16, 24, 20, 28, 18, 26, 22, 64};

const uint8_t fixed_litml_bits[STABLE_SIZE] = {
    7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8,
    9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8,
    8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7,
    8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9,
    8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8,
    8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8,
    8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7,
    8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9,
    7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8,
    9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8,
    8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8,
    8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9,
    7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 8, 7, 8, 8, 9, 7, 8, 8, 9, 8, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8, 9, 7, 8, 8,
    9, 8, 8, 8, 9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5};

const uint16_t fixed_litml_val[STABLE_SIZE] = {
    0,  80,  16, 115,  31, 112,  48, 192,   10, 96,   32, 160,   0,  128,   64,  224, 6,  88,   24, 144,  59,  120,
    56, 208, 17, 104,  40, 176,  8,  136,   72, 240,  4,  84,    20, 227,   43,  116, 52, 200,  13, 100,  36,  168,
    4,  132, 68, 232,  8,  92,   28, 152,   83, 124,  60, 216,   23, 108,   44,  184, 12, 140,  76, 248,  3,   82,
    18, 163, 35, 114,  50, 196,  11, 98,    34, 164,  2,  130,   66, 228,   7,   90,  26, 148,  67, 122,  58,  212,
    19, 106, 42, 180,  10, 138,  74, 244,   5,  86,   22, 0,     51, 118,   54,  204, 15, 102,  38, 172,  6,   134,
    70, 236, 9,  94,   30, 156,  99, 126,   62, 220,  27, 110,   46, 188,   14,  142, 78, 252,  0,  81,   17,  131,
    31, 113, 49, 194,  10, 97,   33, 162,   1,  129,  65, 226,   6,  89,    25,  146, 59, 121,  57, 210,  17,  105,
    41, 178, 9,  137,  73, 242,  4,  85,    21, 258,  43, 117,   53, 202,   13,  101, 37, 170,  5,  133,  69,  234,
    8,  93,  29, 154,  83, 125,  61, 218,   23, 109,  45, 186,   13, 141,   77,  250, 3,  83,   19, 195,  35,  115,
    51, 198, 11, 99,   35, 166,  3,  131,   67, 230,  7,  91,    27, 150,   67,  123, 59, 214,  19, 107,  43,  182,
    11, 139, 75, 246,  5,  87,   23, 0,     51, 119,  55, 206,   15, 103,   39,  174, 7,  135,  71, 238,  9,   95,
    31, 158, 99, 127,  63, 222,  27, 111,   47, 190,  15, 143,   79, 254,   0,   80,  16, 115,  31, 112,  48,  193,
    10, 96,  32, 161,  0,  128,  64, 225,   6,  88,   24, 145,   59, 120,   56,  209, 17, 104,  40, 177,  8,   136,
    72, 241, 4,  84,   20, 227,  43, 116,   52, 201,  13, 100,   36, 169,   4,   132, 68, 233,  8,  92,   28,  153,
    83, 124, 60, 217,  23, 108,  44, 185,   12, 140,  76, 249,   3,  82,    18,  163, 35, 114,  50, 197,  11,  98,
    34, 165, 2,  130,  66, 229,  7,  90,    26, 149,  67, 122,   58, 213,   19,  106, 42, 181,  10, 138,  74,  245,
    5,  86,  22, 0,    51, 118,  54, 205,   15, 102,  38, 173,   6,  134,   70,  237, 9,  94,   30, 157,  99,  126,
    62, 221, 27, 110,  46, 189,  14, 142,   78, 253,  0,  81,    17, 131,   31,  113, 49, 195,  10, 97,   33,  163,
    1,  129, 65, 227,  6,  89,   25, 147,   59, 121,  57, 211,   17, 105,   41,  179, 9,  137,  73, 243,  4,   85,
    21, 258, 43, 117,  53, 203,  13, 101,   37, 171,  5,  133,   69, 235,   8,   93,  29, 155,  83, 125,  61,  219,
    23, 109, 45, 187,  13, 141,  77, 251,   3,  83,   19, 195,   35, 115,   51,  199, 11, 99,   35, 167,  3,   131,
    67, 231, 7,  91,   27, 151,  67, 123,   59, 215,  19, 107,   43, 183,   11,  139, 75, 247,  5,  87,   23,  0,
    51, 119, 55, 207,  15, 103,  39, 175,   7,  135,  71, 239,   9,  95,    31,  159, 99, 127,  63, 223,  27,  111,
    47, 191, 15, 143,  79, 255,  1,  257,   17, 4097, 5,  1025,  65, 16385, 3,   513, 33, 8193, 9,  2049, 129, 0,
    2,  385, 25, 6145, 7,  1537, 97, 24577, 4,  769,  49, 12289, 13, 3073,  193, 0};
