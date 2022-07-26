"""Suvarnabhumi Airport"""

def cal1(total, pam, fls2, mnt):
    """D๋"""
    if total > 12 and pam == ("PM"):
        total -= 11
        pam = ("AM")
        print("BBK - %s" %fls2)
        print("%02d:%d %s" %(total, mnt, pam))
    elif total > 12 and pam == ("AM"):
        total -= 11
        pam = ("PM")
        print("BBK - %s" %fls2)
        print("%02d:%d %s" %(total, mnt, pam))
    elif total < 12 and pam == ("PM"):
        pam = ("PM")
        print("BBK - %s" %fls2)
        print("%02d:%d %s" %(total, mnt, pam))
    elif total < 12 and pam == ("PM"):
        pam = ("PM")
        print("BBK - %s" %fls2)
        print("%02d:%d %s" %(total, mnt, pam))

def cal2(total, pam, fls2, total1):
    """D๋"""
    if total > 12 and pam == ("PM"):
        total -= 12
        pam = ("AM")
        print("BBK - %s" %fls2)
        print("%02d:%d %s" %(total, total1, pam))
    elif total > 12 and pam == ("AM"):
        total -= 12
        pam = ("PM")
        print("BBK - %s" %fls2)
        print("%02d:%d %s" %(total, total1, pam))
    elif total < 12 and pam == ("PM"):
        pam = ("PM")
        print("BBK - %s" %fls2)
        print("%02d:%d %s" %(total, total1, pam))
    elif total < 12 and pam == ("PM"):
        pam = ("PM")
        print("BBK - %s" %fls2)
        print("%02d:%d %s" %(total, total1, pam))


def main():
    """D๋"""
    input()
    stp = input()
    tme = input()
    tme_new = tme.split(":")
    hrs = int(tme_new[0])
    mnt_zero = tme_new[1]
    mnt_one = mnt_zero.split(" ")
    mnt = int(mnt_one[0])
    pam = mnt_one[1].upper()
    fls = stp.split("(", )
    fls1 = str(fls[1])
    fls2 = fls1[:-1]
    if stp == ("To Sydney (SYD)"):
        total = hrs + 11
        cal1(total, pam, fls2, mnt)

    elif stp == ("To Ho Chi Minh (SGN)"):
        total = hrs + 1
        total1 = mnt + 50
        if total1 >= 60:
            total += 1
            total1 -= 60
        cal2(total, pam, fls2, total1)

    elif stp == ("To Atlanta Georgia  (ATL)"):
        total = hrs + 9
        total1 = mnt + 55
        if total1 >= 60:
            total += 1
            total1 -= 60
        cal2(total, pam, fls2, total1)

    elif stp == ("To Vancouver Canada(YVR)"):
        total = hrs + 2
        total1 = mnt + 20
        if total1 >= 60:
            total += 1
            total1 -= 60
        cal2(total, pam, fls2, total1)

    elif stp == ("To Kathmandu (KTM)"):
        total = hrs + 11
        total1 = mnt + 45
        if total1 >= 60:
            total += 1
            total1 -= 60
        cal2(total, pam, fls2, total1)

main()
