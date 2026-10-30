#前[0-6]是星期1-7 後[0-11]是節數1-9 a-c
#curriculum = [["" for _ in range(12)] for _ in range(7)]
curriculum3 = [["" for _ in range(12)] for _ in range(7)]
curriculum4 = [["" for _ in range(12)] for _ in range(7)]
curriculum5 = [["" for _ in range(12)] for _ in range(7)]
curriculum6 = [["" for _ in range(12)] for _ in range(7)]
curriculum7 = [["" for _ in range(12)] for _ in range(7)]
curriculum8 = [["" for _ in range(12)] for _ in range(7)]
curriculum9 = [["" for _ in range(12)] for _ in range(7)]

#只有必修21學分
curriculum3[0][2] = curriculum3[0][3] = curriculum3[4][2] = "CS008"
curriculum3[0][4] = curriculum3[0][5] = "CS004"
curriculum3[0][6] = curriculum3[1][0] = curriculum3[1][1] = "CS007"
curriculum3[1][2] = curriculum3[4][0] = curriculum3[4][1] = "CS006"
curriculum3[1][7] = curriculum3[1][8] = curriculum3[1][9] = "CS001"
curriculum3[2][1] = curriculum3[2][2] = curriculum3[2][3] = "CS005"
curriculum3[3][2] = curriculum3[3][3] = "CS003"
curriculum3[4][9] = curriculum3[4][10] = "CS013"
#全必修+1選修23學分
curriculum4[0][2] = curriculum4[0][3] = curriculum4[4][2] = "CS008"
curriculum4[0][4] = curriculum4[0][5] = "CS004"
curriculum4[0][6] = curriculum4[1][0] = curriculum4[1][1] = "CS007"
curriculum4[1][2] = curriculum4[4][0] = curriculum4[4][1] = "CS006"
curriculum4[1][7] = curriculum4[1][8] = curriculum4[1][9] = "CS001"
curriculum4[2][1] = curriculum4[2][2] = curriculum4[2][3] = "CS005"
curriculum4[3][2] = curriculum4[3][3] = "CS003"
curriculum4[3][7] = curriculum4[3][6] = "CS014"
curriculum4[4][5] = curriculum4[4][6] = "CS018"
#25學分不能再加選課程
curriculum5[0][2] = curriculum5[0][3] = curriculum5[4][2] = "CS008"
curriculum5[0][4] = curriculum5[0][5] = "CS004"
curriculum5[0][6] = curriculum5[1][0] = curriculum5[1][1] = "CS007"
curriculum5[1][2] = curriculum5[4][0] = curriculum5[4][1] = "CS006"
curriculum5[1][7] = curriculum5[1][8] = curriculum5[1][9] = "CS001"
curriculum5[2][1] = curriculum5[2][2] = curriculum5[2][3] = "CS005"
curriculum5[2][5] = curriculum5[2][6] = "CS017"
curriculum5[3][2] = curriculum5[3][3] = "CS003"
curriculum5[4][5] = curriculum5[4][6] = "CS019"
curriculum5[4][9] = curriculum5[4][10] = "CS013"
#學分25但沒修到必修要退選選修(EX: 職場倫理和數邏)
curriculum6[0][4] = curriculum6[0][5] = "CS004"
curriculum6[0][6] = curriculum6[1][0] = curriculum6[1][1] = "CS007"
curriculum6[0][7] = curriculum6[0][8] = curriculum6[4][3] = "CS009"
curriculum6[1][2] = curriculum6[4][0] = curriculum6[4][1] = "CS006"
curriculum6[1][7] = curriculum6[1][8] = curriculum6[1][9] = "CS001"
curriculum6[2][1] = curriculum6[2][2] = curriculum6[2][3] = "CS005"
curriculum6[2][5] = curriculum6[2][6] = curriculum6[4][4] = "CS010"
curriculum6[3][2] = curriculum6[3][3] = "CS003"
curriculum6[4][9] = curriculum6[4][10] = "CS013"
#19學分要加選體育2但已滿
curriculum7[0][4] = curriculum7[0][5] = "CS004"
curriculum7[0][6] = curriculum7[1][0] = curriculum7[1][1] = "CS007"
curriculum7[0][7] = curriculum7[0][8] = curriculum7[4][3] = "CS009"
curriculum7[1][2] = curriculum7[4][0] = curriculum7[4][1] = "CS006"
curriculum7[1][7] = curriculum7[1][8] = curriculum7[1][9] = "CS001"
curriculum7[2][1] = curriculum7[2][2] = curriculum7[2][3] = "CS005"
curriculum7[3][2] = curriculum7[3][3] = "CS003"
curriculum7[4][9] = curriculum7[4][10] = "CS013"
#5分(修不到8學分
curriculum8[0][6] = curriculum8[1][0] = curriculum8[1][1] = "CS007"
curriculum8[4][5] = curriculum8[4][6] = "CS019"
#21學分
curriculum9[0][2] = curriculum9[0][3] = curriculum9[4][2] = "CS008"
curriculum9[0][4] = curriculum9[0][5] = "CS004"
curriculum9[0][6] = curriculum9[1][0] = curriculum9[1][1] = "CS007"
curriculum9[0][8] = curriculum9[0][9] = "A06"
curriculum9[1][2] = curriculum9[4][0] = curriculum9[4][1] = "CS006"
curriculum9[1][7] = curriculum9[1][8] = curriculum9[1][9] = "CS001"
curriculum9[2][1] = curriculum9[2][2] = curriculum9[2][3] = "CS005"
curriculum9[3][2] = curriculum9[3][3] = "CS003"
curriculum9[4][9] = curriculum9[4][10] = "CS013"

#學生[id,name,dept,credits_limit,enrolled(課程表)]
students = [[1150101,"王曉明","資工一",25,curriculum3],
            [1150102,"赤羽葉","資工一",25,curriculum3],
            [1150103,"沈佳宜","資工一",25,curriculum4],
            [1150104,"毛利藍","資工一",25,curriculum5],
            [1150105,"森德綸","資工一",25,curriculum6],
            [1150106,"伏黑惠","資工一",25,curriculum7],
            [1150107,"洪菁晴","資工一",25,curriculum8],
            [1150108,"月島螢","資工一",25,curriculum9],
            [1150109,"柯景騰","資工一",25,curriculum3],
            [1150110,"徐太宇","資工一",25,curriculum3],
            [1140120,"夜神月","資工二",25,curriculum4],
            [1140131,"林真心","資工二",25,curriculum5],
            [1140146,"五條悟","資工二",25,curriculum6],
            [1130116,"八千代","資工三",25,curriculum7],
            [1130124,"芙莉蓮","資工三",25,curriculum8]]

#[code代碼,name名稱,credits學分,type必選修,teacher教師,capacity人數限制,current目前人數,room教室,[slots時段]]
course = [
["CS001","程式設計",3,"必修","郭大爺",45,40,"06206",["2-9","2-a"]],
["CS002","日文",2,"選修","鄭要學",30,0,"03303",["2-7","2-8"]],
["CS003","國文",2,"必修","陳詩雅",40,30,"06306",["4-3","4-4"]],
["CS004","英文",2,"必修","李古德",40,30,"02303",["1-5","1-6"]],
["CS005","微積分",3,"必修","林倍",40,30,"06302",["3-2","3-3","3-4"]],
["CS006","線性代數",3,"必修","何偉",45,44,"06206",["2-3","5-1","5-2"]],
["CS007","計算機概論",3,"必修","江心蔡",40,30,"06302",["1-7","2-1","2-2"]],
["CS008","數位邏輯設計",3,"必修","林凱",40,35,"06302",["1-3","1-4","5-3"]],
["CS009","資料結構",3,"選修","吳廣",40,30,"02303",["1-8","1-9","5-4"]],
["CS010","工程數學",3,"選修","王傑",45,35,"06206",["3-6","3-7","5-5"]],
["CS011","物理實驗",3,"選修","金潛",30,30,"03303",["3-8","3-9","3-a"]],
["CS012","職場倫理",2,"選修","詹姆士",40,30,"06302",["5-3","5-4"]],
["CS013","體育(1)",2,"必修","李多會",50,25,"00101",["5-b","5-c"]],
["CS014","體育(2)",2,"必修","安境",50,50,"00101",["4-7","4-8"]],
["CS015","基本設計",3,"選修","洪水",45,35,"06206",["2-4","2-5","4-5"]],
["CS016","資訊與生活",2,"選修","菜究戀",40,30,"02303",["1-2","1-3"]],
["CS017","心理與人生",2,"選修","李雲",30,20,"03303",["3-5","3-6"]],
["CS018","創新與創業",2,"選修","吳狄",40,25,"06302",["5-6","5-7"]],
["CS019","藝術概論",2,"選修","章逾稍",40,20,"02303",["4-6","4-7"]],
["CS020","親密關係",2,"選修","楊妹咩",30,25,"03303",["4-a","4-b"]]]

#activitys[id,name,date,slots,current目前人數,need_capacity人數限制,room]
activitys=[
['A01','火舞社表演','10/13','5-7',30,10,'02303'],
['A02','自主學Python','10/22','4-4',40,15,'06206'],
['A03','技藝競賽培養','11/2','1-5',30,10,'03303'],
['A04','慈濟社活動','11/14',['6-6','6-7'],40,20,'06206'],
["A05","弓道社社課","11/22",["7-3","7-4"],40,20,"06206"],
["A06","口技社","10/19",["1-9","1-a"],45,15,"06206"],
["A07","熱舞表演","10/23","5-9",50,30,"00101"],
["A08","排球冠亞軍賽","10/17",["6-3","6-4"],50.24,"00101"],
["A09","網球競賽","10/09",["5-a","5-b"],50,20,"00101"],
["A10","直笛表演","10/21","3-3",40,15,"06302"]
]

#教室[id,capacity]
classroom = [
["06206",45],
["03303",30],
["06302",40],
["02303",40],
["00101",50]]
