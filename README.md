# flying-chess-game
This is a flying chess game, is written with python , hope to bring you some fun O(∩_∩)O

## **Game introduction and rules**
### Map ###
● The map is randomly generated, and here are the results of opening the game five times  
![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/screenshot_01_A.png)![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/screenshot_02_B.png)![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/screenshot_03_C.png)![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/screenshot_04_D.png)![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/screenshot_05_E.png)  

● 这是一个双人游戏，需要两位玩家来分别扮演A与B。  

### PlayerA ###
![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/playerA_A.png)  
### PlayerB ###
![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/playerB_B.png)  

● 游戏开始后请按A键掷骰子，骰子的点数是0到6（0到6随机抽取数字，是有可能抽到0的，随机到的数字就是玩家本轮可以行走的步数）  

● 地图上有一些特殊的格子，他们分别有着不同的功能：  
### Switch Grid ###
Has the function of allowing player A to switch positions with player B  

![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/exchangeGrid_E.png)  
### BackUp Grid ###
Make the player go back a random number of steps (1~6)  

![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/BackUpGrid_B.png)  
### Cross Grid ###
Let the player cross over to the next same grid  

![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/crossGrid_C.png)  
### Win Grid ###
The first player to reach this grid wins  

![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/finalGrid_F.png)  
### Common Grid ###
The most common grid, they do nothing  

![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/normalGrid_N.png)  
### Corner Grid ###
They are at the corner of every line of the map, and have no function  

![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/cornerGrid_C.png)  

● Please pay attention to the prompt bar at the bottom of the screen, it will tell you whose turn is now, and the random number of steps forward or backward  
### Bottom tip area ###
![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/tips_A_A.png)  
![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/tips_B.png)  
![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/tips_C.png)  
## **Screen recording**

## **Game screenshot**
![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/gamePanle.png)  
![image](https://github.com/cobalt-sv/flying-chess-game/blob/main/img/winPanle.png)  
## **Tips**
●If you want to download it to play, you need to download all the files in src (source code) and files (resource files)  
●The game still has some bugs, such as during A's turn, A steps on the switch grid, and after A and B switch positions, A lands on the cross grid, which causes the positions of A and B to be displayed incorrectly(This bug does not affect the continuation of the game)

