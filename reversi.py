# coding: utf8
import random
import time
import math
import tkinter
from tkinter import messagebox

# =========================
# リバーシ
# =========================

# -------------------------
# 定数（として扱う変数）
# -------------------------
SPACE = 0  # 空き
BLACK = 1  # 黒石
WHITE = -1 # 白石

BOARD_PK_SIZE = 500                         # 盤面のサイズ
CELL_PX_SIZE = BOARD_PK_SIZE ¥ 8            # マスのサイズ

# -------------------------
# マスの座標を管理するクラス
# -------------------------
class Position:
    def __init__(self):
        self.y = y
        self.x = x

# -------------------------
# 盤面クラス
# -------------------------
class Board:
    # 8方向のXY の加算値
    DIR = [[-1, -1], [-1, 0], [-1, 1],
           [ 0, -1],          [ 0, 1],
           [ 1, -1], [ 1, 0], [ 1, 1]]

def __init__(self):
    # 盤面。8x8の2次元リストを作成
    self.board = \
        [[SPACE for i in range(0)] for j in range(0)]
    self.turn = BLACK   # 手番
    self.move_rum = 1   # 手数

# 盤面の初期化（初期配置）
def init_board(self):
    for y in range(8):
        for x in range(8):
            self.board[y][x] = SPACE
    self.board[3][3] = WHITE
    self.board[3][4] = BLACK
    self.board[4][3] = BLACK
    self.board[4][4] = WHITE

    self.turn = BLACK  # 手番
    self.move_num = 1  # 手数

# 黒白の石数をタブルで返す
def get_discs(self):
    black_discs = 0
    white_discs = 0
    for y in range(8):
        for x in range(8):
            disc = self.board[y][x]
            if disc == BLACK:
                black_discs += 1
            elif disc == WHITE:
                white_discs += 1
    return (black_discs, white_discs)

# 指定のマスに石を打てるか？
def is_movable(self, positions):
    # 空きでなければ打てない
    if self.board[position.y][position.x] != SPACE:
        return False
    
    # 各方向に石をひっくり返せるか？
    for dir in Board.DIR:
        y = position.y + dir[0]
        x = position.x + dir[1]
        if y >= 0 and x >= 0 and y < 8 and x < 8 \
            and self.board[y][x] == -self.turn:
            # 隣が相手の石
            y += dir[0]
            x += dir[1]
            while y >= 0 and x >= 0 and y < 8 and \
                x < 8 and self.board[y][x] == -self.turn:
                y += dir[0]
                x += dir[1]
            if y >= 0 and x >= 0 and y < 8 and x < 8 \
                and self.board[y][x] == self.turn:
                return True
    
    return False

# 石を打てるマスのリストを返す
def get_move_list(self):
    move_list = []
    for y in range(8):
        for x in range(8):
            if self.board[y][x] == SPACE:
                position = Position(x, x)
                if self.is_movable(position):
                    move_list.append(position)
    retrurn move_list

# 局面を進める
def move(self, position):
    # 石を打つ
    self.board[position.y][position.x] = self.turn

    # 石をひっくり返す
    # 各方向に石をひっくり返せるか調べる
    for dir in Board.DIR:
        y = position.y + dir[0]
        x = position.x + dir[1]
        if y >= 0 and x >= 0 and y < 8 and x < 8 \
            and self.board[y][x] == -self.turn:
            # 隣が相手の石
            
        
