#
# Run with: python3 test_clangd_clang-tidy.py --log --log-pretty "/path/to/clangd --compile-commands-dir ${PWD}/cpp-test/build-1"
#

import ls_interact as ls
from common import JsonRpc
import os


def interact(json_rpc):

    paths = [os.getcwd() + '/cpp-test/src/first.cpp']

    for p in paths:
        json_rpc.notify(ls.DidOpenTextDocument(p))

    for p in paths:
        json_rpc.wait_for(JsonRpc.JsonRpcPendingMethod(
            'textDocument/publishDiagnostics'))


def main():
    ret = os.system('make -C cpp-test/build-1')
    if ret != 0:
        return ret

    ls.run(interact, cmdline_args="--clang-tidy=true --clang-tidy-checks='bugprone-*'", initialize_params={
        'rootUri': 'file://' + os.getcwd() + '/cpp-test/src',
    })


if __name__ == '__main__':
    main()
