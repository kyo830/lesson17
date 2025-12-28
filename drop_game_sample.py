import pyxel
import random
import time

apples = []

pyxel.init(250, 200, title="apples")

apples = [{
          "x":random.randint(1,pyxel.width+1),
          "y":random.randint(1,100),
          "speed":1,
          "alive":True,
          "score":random.randint(1,3)
}for _ in range(100)]

print(apples)


player = {"x": 10, "y": pyxel.height - 25, "w": 15, "h": 20, "speed": 10}

score = 0
time_limit = 10
start_time = time.time()
# 当たり判定を調べる関数
def is_hit(player, apple):
    if(player["x"] < apple["x"] + 10 and
           player["x"] + player["w"] > apple["x"] and
           player["y"] < apple["y"] + 10 and
           player["y"] + player["h"] > apple["y"]):
        return True
    else:
        return False

def update():
    global apples, score
    
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        pyxel.quit()
        print(apples)
    # プレイヤーの移動
    # 右移動
    if pyxel.btn(pyxel.KEY_RIGHT):
        player["x"] += player["speed"]
    
    # 左移動
    if pyxel.btn(pyxel.KEY_LEFT):
        player["x"] -= player["speed"]

    # リンゴの落下
    for apple in apples:
        apple["y"] += apple["speed"]

        # もしリンゴが画面の下端を超えたら
        if apple["y"] > pyxel.height:
            # 生存フラグをFalseにする
            apple["alive"] = False
        
        # リンゴとプレイヤーの衝突判定
        if(is_hit(player, apple)):
            
            # 当たった場合の処理
            apple["alive"] = False
            score += apple["score"]
    

    # 生きているリンゴ(alive = True)だけを集めて新しいリストを作る
    new_apples = [] # 新しいリストを用意
    for apple in apples:
        if apple["alive"]: # もしリンゴが生きていたら
            new_apples.append(apple) # 新しいリストに追加
        else:
            new_apples.append( {
          "x":random.randint(1,pyxel.width+1),
          "y":random.randint(1,100),
          "speed":1,
          "alive":True,
          "score":random.randint(1,3)
})
    # 元のリストを新しいリストで上書き
    apples = new_apples



def draw():
    pyxel.cls(0)
    for apple in apples:
        if apple["alive"]:
            pyxel.rect(apple["x"], apple["y"], 7, 10, 8)
             
        else:
            apple["y"] = 10
            apple["alive"] = True
            pyxel.rect(apple["x"], apple["y"], 10, 10, 8)
    
 
    remaining_time = max(0,time_limit - int(time.time()-start_time))
    pyxel.text(10,10,f"Time:{remaining_time}",7)
    
    pyxel.rect(player["x"], player["y"], player["w"], player["h"], 5)
    pyxel.text(200, 10, f"Score: {score}", 7)

pyxel.run(update, draw)