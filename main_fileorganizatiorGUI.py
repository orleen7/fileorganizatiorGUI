
"""
Project: Automated File Sorter
Author: Hyori Park
Date: 2026.01.
Description: 
    Regex 기반의 학사 파일 자동 분류 및 NFD/NFC 인코딩 정규화 툴.
    CLI 및 Tkinter GUI 환경을 모두 지원합니다.
"""



import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import re ## 비정형 파일명 패턴 매칭 (학번_이름_유형)
import unicodedata #mac(nfd)->window(nfc) 자소분리현상 해결

def inf(filename):
    week_mat = re.search(r'(\d+)주차', filename)
    id_mat = re.search(r'(\d{8,10})', filename)

    if week_mat and id_mat:
        return week_mat.group(1), id_mat.group(1)
    else:
        return None, None

def organiz():
    target_folder = ent_path.get()
    
    if not target_folder:
        messagebox.showwarning("알림", "폴더를 선택해주세요.")
        return

    raw_text = txt_stu.get("1.0", tk.END)
    req_stu = set(filter(None, re.split(r'[,\s]+', raw_text)))

    try:
        all_files = os.listdir(target_folder)
    except:
        messagebox.showwarning("에러", "경로를 확인해주세요.")
        return

    success_cnt = 0
    fail_cnt = 0
    sub_stu = set()

    for i, filename in enumerate(all_files):
        ###수정한부qns
        print(f"{i}/{len(all_files)} 처리 중: {filename}")
        
        og_path = os.path.join(target_folder, filename)
        
        if os.path.isdir(og_path):
            continue

        fix_name = unicodedata.normalize('NFC', filename)
        week, stu_id = inf(fix_name)

        if week and stu_id:
            week_dir = os.path.join(target_folder, f"{week}주차")
            
            if not os.path.exists(week_dir):
                os.makedirs(week_dir)

            shutil.move(og_path, os.path.join(week_dir, fix_name))
            
            sub_stu.add(stu_id)
            success_cnt += 1
            
        else:
            unknown_dir = os.path.join(target_folder, "확인필요_미분류")
            
            if not os.path.exists(unknown_dir):
                os.makedirs(unknown_dir)
                
            shutil.move(og_path, os.path.join(unknown_dir, fix_name))
            fail_cnt += 1

    msg = f"완료!\n성공: {success_cnt}개\n미분류: {fail_cnt}개"

    if req_stu:
        missing = req_stu - sub_stu
        if missing:
            missing_list = ", ".join(sorted(missing))
            messagebox.showwarning("누락자 발생", msg + f"\n\n[안 낸 사람]\n{missing_list}")
        else:
            messagebox.showinfo("성공", msg + "\n\n전원 제출 완료!")
    else:
        messagebox.showinfo("성공", msg)

def find_f():
    path = filedialog.askdirectory()
    if path:
        ent_path.delete(0, tk.END)
        ent_path.insert(0, path)

root = tk.Tk()
root.title("과제 분류기 (자소분리 해결)")
root.geometry("400x480")

f1 = tk.LabelFrame(root, text="1. 폴더 선택", padx=10, pady=10)
f1.pack(padx=10, pady=5, fill="x")

ent_path = tk.Entry(f1, width=35)
ent_path.pack(side="left", padx=5)

tk.Button(f1, text="찾기", command=find_f).pack(side="right")

f2 = tk.LabelFrame(root, text="2. 학생 명단 (없어도 됨)", padx=10, pady=10)
f2.pack(padx=10, pady=5, fill="both", expand=True)

tk.Label(f2, text="학번 붙여넣기 (콤마나 엔터로 구분)").pack(anchor="w")

txt_stu = tk.Text(f2, height=8, width=40)
txt_stu.pack(pady=5)

tk.Button(root, text="분류 시작", command=organiz, bg="yellow", height=2).pack(pady=10, fill="x", padx=20)

root.mainloop()
