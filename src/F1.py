import model


def add_course():#新增新的課程
    new_course=[]
    new_course.append(input("課程代碼:"))
    new_course.append(input("課程名稱:"))
    new_course.append(int(input("學分:")))
    new_course.append(input("必修/選修:"))
    new_course.append(input("教師:"))
    new_course.append(int(input("人數限制:")))
    new_course.append(0)#目前人數
    new_course.append(input("教室代碼:"))
    t=int(input("一周幾節課:"))
    new_course.append([input(f"時段{j+1}:") for j in range(t)])#時段

    check_new_course(new_course,t)#檢查是否衝堂
    
def check_new_course(new_course,t):#檢查是否衝堂
    s=0#s=0的話表示沒有錯誤
    for i in range(len(model.course)):#取預設課程總共數量
        if new_course[0]==model.course[i][0]:#檢查課程代碼是否重複
            print("報錯拒絕,提示:課程代碼重複")
            s=1
            break
        elif new_course[2]>0:#檢查學分是否為正數
            if new_course[5]>=1:#檢查人數限制是否大於等於1
                continue
            else:
                print("報錯拒絕,提示:人數限制必須大於等於1")
                s=1
                break
        else:
            print("報錯拒絕,提示:學分必須為正數")
            s=1
            break
    if s==0:#s=0的话执行  時段格式是否正確
        for j in new_course[8]:#取新的節數次數
            if j[0] in "1234567":#检查新的课程时段时间是否为星期1-7
                if j[2] in "123456789abc":#检查新的课程时段时间是否为节数1-9 a-c
                    continue
                else:
                    print("報錯拒絕,提示:時段格式不正確")
                    s=1
                    break
            else:
                print("報錯拒絕,提示:時段格式不正確")
                s=1
                break
    if s ==0:
        print("回報成功")
        model.course.append(new_course)#新增課程

def delete_course():#刪除課程
    code=input("請輸入要刪除的課程代碼:")
    j=0#如果輸入錯誤代號執行
    for i in range(len(model.course)):#取預設課程總共數量
        if code==model.course[i][0]:#檢查課程代碼是否存在
            if model.course[i][6]==0:#檢查目前人數是否為0
                model.course.pop(i)#刪除課程
                print("回報成功")
                j=1
                break
            else:
                print("拒絕刪除,提示:請先執行退選或課程取消")
                j=1
                break
    if j==0:
        print("錯誤,提示:課程代碼不存在")
#add_course()#測試
#delete_course()
