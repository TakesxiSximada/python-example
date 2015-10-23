# -*- coding: utf-8 -*-
u"""PEP 471 - os.scandir() function – a better and faster directory iterator

https://docs.python.org/3/whatsnew/3.5.html#pep-471-os-scandir-function-a-better-and-faster-directory-iterator

```
PEP 471 adds a new directory iteration function, os.scandir(), to the standard library.
Additionally, os.walk() is now implemented using scandir,
```

PEP 471は標準ライブラリに新しいディレクトリイテレーションファンクションos.scandir()を追加します。
さらに、os.walk()はos.scandir()を使って現在は実装されています。

```
which makes it 3 to 5 times faster on POSIX systems and 7 to 20 times faster on Windows systems.
```

os.scandir()はPOSIXシステムでは3~5倍、Windowsシステムでは7~20倍高速にします。

```
This is largely achieved by greatly reducing the number of calls to os.stat() required to walk a directory tree.
```

これはディレクトリツリーの走査に必要なos.stat()のコール数を大幅に削減することにより達成されました。

```
Additionally, scandir returns an iterator, as opposed to returning a list of file names,
which improves memory efficiency when iterating over very large directories.
```

さらに、scandirはファイル名のリストを返すのとは対照的に、イテレータを返します。
とても大きなディレクトリの反復処理時に大幅にメモリ効率を改善します。

```
The following example shows a simple use of os.scandir() to display all the files (excluding directories) in the given path that don’t start with '.'
```

次の例では、与えたpathの '.' で始まらない全てのファイル(ディレクトリを除く) を表示する簡単なos.dir()の使い方を示しています。

```
The entry.is_file() call will generally not make an additional system call
```

`entry.is_file()` は一般的に追加のシステムコールをすることはありません。

>>> for entry in os.scandir(path):
...    if not entry.name.startswith('.') and entry.is_file():
...        print(entry.name)

```
See also
PEP 471 – os.scandir() function – a better and faster directory iterator
PEP written and implemented by Ben Hoyt with the help of Victor Stinner.
```

参照
PEP 471 – os.scandir() function – a better and faster directory iterator
PEP written and implemented by Ben Hoyt with the help of Victor Stinner.
"""

import os

for entry in os.scandir(os.getcwd()):
    print(entry)
