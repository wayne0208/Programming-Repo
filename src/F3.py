import model


# 查詢學生資料
def find_student(student_id):
    for student in model.students:
        if student_id == student[0]:
            return student
    return None
# 取得學生的課表
def get_curriculum(student):
    curriculum_name = student[4]
    return getattr(model, curriculum_name)
# 將課程代碼轉換成課程名稱
def get_course_name(code):
    for course in model.course:
        if code == course[0]:
            return course[1]

    # 如果不是課程，檢查是不是活動
    for activity in model.activitys:
        if code == activity[0]:
            return activity[1]
    return code
# 將節數轉換成文字
def get_period_name(index):
    if index < 9:
        return str(index + 1)
    elif index == 9:
        return "a"
    elif index == 10:
        return "b"
    else:
        return "c"
# 顯示個人課表
def show_timetable(student):
    curriculum = get_curriculum(student)
    print("\n========== 個人資料 ==========")
    print("學號：", student[0])
    print("姓名：", student[1])
    print("系級：", student[2])
    print("學分上限：", student[3])
    print("\n========== 個人課表 ==========")
    print("節數\t一\t二\t三\t四\t五\t六\t日")
    for i in range(12):
        period = get_period_name(i)
        row = "第" + period + "節"
        for j in range(7):
            code = curriculum[j][i]
            if code != "":
                name = get_course_name(code)
            else:
                name = "—"
            row = row + "\t" + name
        print(row)
    print("==============================")
# 查詢個人空堂
def query_free_time(student):
    curriculum = get_curriculum(student)
    day = input("請輸入星期幾（1～7）：")
    if not day.isdigit() or int(day) < 1 or int(day) > 7:
        print("星期輸入錯誤")
        return
    day = int(day)
    free_periods = []
    # 找出空堂
    for i in range(12):
        if curriculum[day - 1][i] == "":
            free_periods.append(get_period_name(i))
    print("\n星期", day, "的空堂時段：")
    if len(free_periods) == 0:
        print("這一天沒有空堂")
    else:
        for period in free_periods:
            print("第" + period + "節", end=" ")
        print()
    # 查詢連續空堂
    print("\n連續空堂時段：")
    start = -1
    for i in range(12):
        if curriculum[day - 1][i] == "":
            if start == -1:
                start = i
        else:
            if start != -1:
                print(
                    "第" + get_period_name(start) +
                    "節 ～ 第" + get_period_name(i - 1) + "節"
                )
                start = -1
    # 如果最後幾節也是空堂
    if start != -1:
        print(
            "第" + get_period_name(start) +
            "節 ～ 第" + get_period_name(11) + "節"
        )
# F3 主選單
def main():
    student_id = input("請輸入學生學號：")
    if not student_id.isdigit():
        print("學號格式錯誤")
        return
    student = find_student(int(student_id))
    if student == None:
        print("找不到這名學生")
        return
    while True:
        print("\n========== F3 個人課表與空堂查詢 ==========")
        print("1. 查看個人課表")
        print("2. 查詢個人空堂")
        print("0. 離開")
        choice = input("請選擇功能：")
        if choice == "1":
            show_timetable(student)
        elif choice == "2":
            query_free_time(student)
        elif choice == "0":
            print("離開 F3")
            break
        else:
            print("輸入錯誤，請重新選擇")
if __name__ == "__main__":
    main()