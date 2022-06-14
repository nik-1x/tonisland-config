import requests,subprocess
def load(v):
    def r(u):return requests.get(u)
    def cf(n):return c['v'][n]
    def w(f,d):f.write(d); f.close()
    def o(f,t='w'):return open(cf(f),t)
    def b(v):return str(v).lower()
    c=r('https://raw.githubusercontent.com/nikitt-code/tonisland-config/main/wrap.json').json()
    T,F=True,False
    def u_():
        d,p=r(c[cf(0)]).json(),''
        for key in d: p+='{}={}\n'.format(key,d[key])
        with o(0) as p_: w(p_,p);return T
    def e_(v=T):
        with o(4) as e:w(e, 'eula='+(b(T) if v else b(F)));return T
    def d(vr):
        with o(5, 'wb') as p:w(p,r(c[cf(1)].replace('%v',vr)).content);return T
    def r_(): 
        while T:subprocess.call(['java','-jar',cf(5),'-nogui'])
    if d(v)&e_(T)&u_():r_()
load('1.19')