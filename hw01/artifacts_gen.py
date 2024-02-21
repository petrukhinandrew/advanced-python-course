from sys import argv, stdin
from subprocess import check_output

if __name__ == '__main__':
    assert argv[2] in ['wc.py', 'nl.py', 'tail.py', '.\\wc.py',
                       '.\\nl.py', '.\\tail.py'], f'no app found for {argv[2]}'

    test_spec = argv[1]
    proxy_stdin = test_spec == 'stdin'
    out_fname = 'artifacts/' + argv[2].strip()[:-3] + '_' + test_spec + '.txt'
    proxy_cmd = 'python3 ' + ' '.join(argv[2:])

    with open(out_fname, 'w') as res:
        res.write(f'{proxy_cmd}\n')
        if proxy_stdin:
            inp = stdin.read()
        res.write(check_output(proxy_cmd, shell=True,
                  input=inp if proxy_stdin else None, universal_newlines=True))
        if proxy_stdin:
            res.write('with input:\n')
            res.write(inp)
