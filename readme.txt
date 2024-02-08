重力崩壊の数値的シミュレーション　圧力変化によるOSモデルとの違いについて

＞開発環境
pyenv: Python 3.7.3 (Pypy 3.10-7.3.12)
VSCode 1.85.0
MacBook Air 13-inch, 2020
OS macOS Ventura 13.4.1 (c)
CPU 1.1 GHz クアッドコアIntel Core i5
メモリ 8GB

＞ライブラリ
numpy 1.21.6
matplotlib 3.5.3
scipy 1.6.2


＞説明
scipyを用いて微分方程式を解く。

＞double_pendulum.py
・条件
https://matplotlib.org/stable/gallery/animation/double_pendulum.html

scipyを用いた2重振り子のシミュレーション。
θ1,θ2,ω1,ω2に関する連立微分方程式
1. dΘ/dt = ω1
2. {mLω1^2 sinDcosD + mgsinθ2cosD + mlω2^2 sinD - (M+m)gsinΘ1}
    /{(M+m)L-mLcos^2 D}
3. dθ2/dt = ω2
4. {-m l ω2^2 sinDcosD + (M+m)L ω1^2 sinD - (M+m)gsinθ2}
    /{(M+m)l - mlcos^2 D}
(D = θ2 - θ1)

を、初期条件
g=G (=9.8),
L = L1 (=1.0), l = L2 (=1.0),
M = M1 (=1.0), m = M2 (=1.0),
θ1 = th1 (=120.0), θ2 = th2 (=-10.0)
ω1 = w1 (=0.0), ω2 = w2 (=0.0)
及び、dt = 0.01
である。

・方法
オイラー法を用いる。
derivs関数では、stateの変化量を計算する。
state=[th1,w1,th2,w2]で、
th(角度)の変化量はw(直前の角速度)であり、
wの変化量は微分方程式にそれぞれ従う。


gravitational_collupse1:
    OSモデルに従う。数値的な解と解析的な解を比較し、それが満足するかを確かめる。
    具体的には、r,ρ,n,Uに関する連立微分方程式
    1. r. = U
    2. (nr^2)./nr^2 = -U'/r'
    3. ρ./ρ = n./n
    4. U. = -m/r^2

    を、初期条件
    1: 圧力 p=0
    2: 質量密度 ρ=n=(4πa^3 /3)/(aの長さ)
    3: 半径 r=a
    4: U=0
    (. = d/dt, '=d/da)
    ただし、初期半径r(t)=aを正の定数とし、mは定数とする(m=1)。



