def string_parser():
    str = 'X-DSPAM-Confidence:0.8475'
    col = str.find(':')
    fstr = float(str[col+1:])
    fstr = fstr + 0.025
    nstr = 'Adjusted DSPAM Confidence Score: %g' % fstr
    print(nstr)


if __name__ == "__main__":
    string_parser()
