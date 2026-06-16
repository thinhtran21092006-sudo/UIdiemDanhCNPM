#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Batch runner script for the Student Management System
Chạy tất cả các file dự án theo thứ tự đúng
"""

import subprocess
import sys
import os

def run_setup():
    """Chạy setup_database.py để tạo cơ sở dữ liệu"""
    print("=" * 60)
    print("Bước 1: Thiết lập cơ sở dữ liệu...")
    print("=" * 60)
    
    try:
        result = subprocess.run(
            [sys.executable, "setup_database.py"],
            cwd=os.path.dirname(__file__),
            check=True
        )
        print("\n✓ Cơ sở dữ liệu đã được thiết lập thành công!\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Lỗi khi thiết lập cơ sở dữ liệu: {e}\n")
        return False

def run_gui():
    """Chạy hello_world.py để khởi động GUI"""
    print("=" * 60)
    print("Bước 2: Khởi động giao diện quản lý học sinh...")
    print("=" * 60)
    
    try:
        result = subprocess.run(
            [sys.executable, "hello_world.py"],
            cwd=os.path.dirname(__file__)
        )
        return True
    except Exception as e:
        print(f"\n✗ Lỗi khi chạy giao diện: {e}\n")
        return False

if __name__ == "__main__":
    print("\n🎓 HỆ THỐNG QUẢN LÝ HỌC SINH")
    print("Student Management System\n")
    
    # Kiểm tra xem có tham số dòng lệnh hay không
    if len(sys.argv) > 1:
        if sys.argv[1] == "setup":
            run_setup()
        elif sys.argv[1] == "run":
            run_gui()
        else:
            print("Cách dùng: python run.py [setup|run]")
            print("  setup: Thiết lập cơ sở dữ liệu")
            print("  run: Chạy giao diện")
    else:
        # Mặc định: chạy setup rồi GUI
        if run_setup():
            run_gui()
