def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    mnum = int(input('enter thee number of male student: '))
    fnum = int(input(' enter the number of female students: '))
    
    total = mnum + fnum
    m_perc = mnum / total * 100
    f_perc = fnum / total * 100

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
