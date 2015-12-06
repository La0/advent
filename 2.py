def calc_wrapping(line):
    l,w,h = map(int, line.split('x'))
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

if __name__ == '__main__':
    with open('2.input', 'r') as f:
        print sum([calc_wrapping(l.replace('\n', '')) for l in f.readlines()])
