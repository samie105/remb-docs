---
title: "fs - Node documentation"
source: "https://docs.deno.com/api/node/fs/"
canonical_url: "https://docs.deno.com/api/node/fs/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:06:46.692Z"
content_hash: "fb7ccbf0036a53f6db3b8153684ed5e012ae8a7ad39c801159db847d5cb2dbf7"
menu_path: ["fs - Node documentation"]
section_path: []
content_language: "en"
---
### Usage in Deno

```typescript
import * as mod from "node:fs";
```

The `node:fs` module enables interacting with the file system in a way modeled on standard POSIX functions.

To use the promise-based APIs:

```js
import * as fs from 'node:fs/promises';
```

To use the callback and sync APIs:

```js
import * as fs from 'node:fs';
```

All file system operations have synchronous, callback, and promise-based forms, and are accessible using both CommonJS syntax and ES6 Modules (ESM).

c

[Dir](.././fs/~/Dir "Dir")

A class representing a directory stream.

-   [close](.././fs/~/Dir#method_close_0)
-   [closeSync](.././fs/~/Dir#method_closesync_0)
-   [path](.././fs/~/Dir#property_path)
-   [read](.././fs/~/Dir#method_read_0)
-   [readSync](.././fs/~/Dir#method_readsync_0)

c

[Dirent](.././fs/~/Dirent "Dirent")

A representation of a directory entry, which can be a file or a subdirectory within the directory, as returned by reading from an `fs.Dir`. The directory entry is a combination of the file name and file type pairs.

-   [isBlockDevice](.././fs/~/Dirent#method_isblockdevice_0)
-   [isCharacterDevice](.././fs/~/Dirent#method_ischaracterdevice_0)
-   [isDirectory](.././fs/~/Dirent#method_isdirectory_0)
-   [isFIFO](.././fs/~/Dirent#method_isfifo_0)
-   [isFile](.././fs/~/Dirent#method_isfile_0)
-   [isSocket](.././fs/~/Dirent#method_issocket_0)
-   [isSymbolicLink](.././fs/~/Dirent#method_issymboliclink_0)
-   [name](.././fs/~/Dirent#property_name)
-   [parentPath](.././fs/~/Dirent#property_parentpath)
-   [path](.././fs/~/Dirent#property_path)

c

[ReadStream](.././fs/~/ReadStream "ReadStream")

Instances of `fs.ReadStream` are created and returned using the [createReadStream](.././fs/~/createReadStream) function.

-   [addListener](.././fs/~/ReadStream#method_addlistener_0)
-   [bytesRead](.././fs/~/ReadStream#property_bytesread)
-   [close](.././fs/~/ReadStream#method_close_0)
-   [on](.././fs/~/ReadStream#method_on_0)
-   [once](.././fs/~/ReadStream#method_once_0)
-   [path](.././fs/~/ReadStream#property_path)
-   [pending](.././fs/~/ReadStream#property_pending)
-   [prependListener](.././fs/~/ReadStream#method_prependlistener_0)
-   [prependOnceListener](.././fs/~/ReadStream#method_prependoncelistener_0)

c

[WriteStream](.././fs/~/WriteStream "WriteStream")

-   Extends `stream.Writable`

-   [addListener](.././fs/~/WriteStream#method_addlistener_0)
-   [bytesWritten](.././fs/~/WriteStream#property_byteswritten)
-   [close](.././fs/~/WriteStream#method_close_0)
-   [on](.././fs/~/WriteStream#method_on_0)
-   [once](.././fs/~/WriteStream#method_once_0)
-   [path](.././fs/~/WriteStream#property_path)
-   [pending](.././fs/~/WriteStream#property_pending)
-   [prependListener](.././fs/~/WriteStream#method_prependlistener_0)
-   [prependOnceListener](.././fs/~/WriteStream#method_prependoncelistener_0)

f

[access](.././fs/~/access "access")

Tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g.`fs.constants.W_OK | fs.constants.R_OK`). Check `File access constants` for possible values of `mode`.

f

[accessSync](.././fs/~/accessSync "accessSync")

Synchronously tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g.`fs.constants.W_OK | fs.constants.R_OK`). Check `File access constants` for possible values of `mode`.

f

[appendFile](.././fs/~/appendFile "appendFile")

Asynchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `Buffer`.

f

[appendFileSync](.././fs/~/appendFileSync "appendFileSync")

Synchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `Buffer`.

f

[chmod](.././fs/~/chmod "chmod")

Asynchronously changes the permissions of a file. No arguments other than a possible exception are given to the completion callback.

f

[chmodSync](.././fs/~/chmodSync "chmodSync")

For detailed information, see the documentation of the asynchronous version of this API: [chmod](.././fs/~/chmod).

f

[chown](.././fs/~/chown "chown")

Asynchronously changes owner and group of a file. No arguments other than a possible exception are given to the completion callback.

f

[chownSync](.././fs/~/chownSync "chownSync")

Synchronously changes owner and group of a file. Returns `undefined`. This is the synchronous version of [chown](.././fs/~/chown).

f

[close](.././fs/~/close "close")

Closes the file descriptor. No arguments other than a possible exception are given to the completion callback.

f

[closeSync](.././fs/~/closeSync "closeSync")

Closes the file descriptor. Returns `undefined`.

f

[copyFile](.././fs/~/copyFile "copyFile")

Asynchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists. No arguments other than a possible exception are given to the callback function. Node.js makes no guarantees about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, Node.js will attempt to remove the destination.

f

[copyFileSync](.././fs/~/copyFileSync "copyFileSync")

Synchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists. Returns `undefined`. Node.js makes no guarantees about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, Node.js will attempt to remove the destination.

f

[cp](.././fs/~/cp "cp")

Asynchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.

f

[cpSync](.././fs/~/cpSync "cpSync")

Synchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.

f

[createReadStream](.././fs/~/createReadStream "createReadStream")

`options` can include `start` and `end` values to read a range of bytes from the file instead of the entire file. Both `start` and `end` are inclusive and start counting at 0, allowed values are in the \[0, [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)\] range. If `fd` is specified and `start` is omitted or `undefined`, `fs.createReadStream()` reads sequentially from the current file position. The `encoding` can be any one of those accepted by `Buffer`.

f

[createWriteStream](.././fs/~/createWriteStream "createWriteStream")

`options` may also include a `start` option to allow writing data at some position past the beginning of the file, allowed values are in the \[0, [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)\] range. Modifying a file rather than replacing it may require the `flags` option to be set to `r+` rather than the default `w`. The `encoding` can be any one of those accepted by `Buffer`.

f

[existsSync](.././fs/~/existsSync "existsSync")

Returns `true` if the path exists, `false` otherwise.

f

[fchmod](.././fs/~/fchmod "fchmod")

Sets the permissions on the file. No arguments other than a possible exception are given to the completion callback.

f

[fchmodSync](.././fs/~/fchmodSync "fchmodSync")

Sets the permissions on the file. Returns `undefined`.

f

[fchown](.././fs/~/fchown "fchown")

Sets the owner of the file. No arguments other than a possible exception are given to the completion callback.

f

[fchownSync](.././fs/~/fchownSync "fchownSync")

Sets the owner of the file. Returns `undefined`.

f

[fdatasync](.././fs/~/fdatasync "fdatasync")

Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX [`fdatasync(2)`](http://man7.org/linux/man-pages/man2/fdatasync.2.html) documentation for details. No arguments other than a possible exception are given to the completion callback.

f

[fdatasyncSync](.././fs/~/fdatasyncSync "fdatasyncSync")

Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX [`fdatasync(2)`](http://man7.org/linux/man-pages/man2/fdatasync.2.html) documentation for details. Returns `undefined`.

f

[fstat](.././fs/~/fstat "fstat")

Invokes the callback with the `fs.Stats` for the file descriptor.

f

[fstatSync](.././fs/~/fstatSync "fstatSync")

Retrieves the `fs.Stats` for the file descriptor.

f

[fsync](.././fs/~/fsync "fsync")

Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX [`fsync(2)`](http://man7.org/linux/man-pages/man2/fsync.2.html) documentation for more detail. No arguments other than a possible exception are given to the completion callback.

f

[fsyncSync](.././fs/~/fsyncSync "fsyncSync")

Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX [`fsync(2)`](http://man7.org/linux/man-pages/man2/fsync.2.html) documentation for more detail. Returns `undefined`.

f

[ftruncate](.././fs/~/ftruncate "ftruncate")

Truncates the file descriptor. No arguments other than a possible exception are given to the completion callback.

f

[ftruncateSync](.././fs/~/ftruncateSync "ftruncateSync")

Truncates the file descriptor. Returns `undefined`.

f

[futimes](.././fs/~/futimes "futimes")

Change the file system timestamps of the object referenced by the supplied file descriptor. See [utimes](.././fs/~/utimes).

f

[futimesSync](.././fs/~/futimesSync "futimesSync")

Synchronous version of [futimes](.././fs/~/futimes). Returns `undefined`.

f

[glob](.././fs/~/glob "glob")

Retrieves the files matching the specified pattern.

f

[globSync](.././fs/~/globSync "globSync")

Retrieves the files matching the specified pattern.

f

[lchown](.././fs/~/lchown "lchown")

Set the owner of the symbolic link. No arguments other than a possible exception are given to the completion callback.

f

[lchownSync](.././fs/~/lchownSync "lchownSync")

Set the owner for the path. Returns `undefined`.

f

[link](.././fs/~/link "link")

Creates a new link from the `existingPath` to the `newPath`. See the POSIX [`link(2)`](http://man7.org/linux/man-pages/man2/link.2.html) documentation for more detail. No arguments other than a possible exception are given to the completion callback.

f

[linkSync](.././fs/~/linkSync "linkSync")

Creates a new link from the `existingPath` to the `newPath`. See the POSIX [`link(2)`](http://man7.org/linux/man-pages/man2/link.2.html) documentation for more detail. Returns `undefined`.

f

[lstat](.././fs/~/lstat "lstat")

Retrieves the `fs.Stats` for the symbolic link referred to by the path. The callback gets two arguments `(err, stats)` where `stats` is a `fs.Stats` object. `lstat()` is identical to `stat()`, except that if `path` is a symbolic link, then the link itself is stat-ed, not the file that it refers to.

f

[lutimes](.././fs/~/lutimes "lutimes")

Changes the access and modification times of a file in the same way as [utimes](.././fs/~/utimes), with the difference that if the path refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link itself are changed.

f

[lutimesSync](.././fs/~/lutimesSync "lutimesSync")

Change the file system timestamps of the symbolic link referenced by `path`. Returns `undefined`, or throws an exception when parameters are incorrect or the operation fails. This is the synchronous version of [lutimes](.././fs/~/lutimes).

f

[mkdir](.././fs/~/mkdir "mkdir")

Asynchronously creates a directory.

f

[mkdirSync](.././fs/~/mkdirSync "mkdirSync")

Synchronously creates a directory. Returns `undefined`, or if `recursive` is `true`, the first directory path created. This is the synchronous version of [mkdir](.././fs/~/mkdir).

f

[mkdtemp](.././fs/~/mkdtemp "mkdtemp")

Creates a unique temporary directory.

f

[mkdtempSync](.././fs/~/mkdtempSync "mkdtempSync")

Returns the created directory path.

f

[open](.././fs/~/open "open")

Asynchronous file open. See the POSIX [`open(2)`](http://man7.org/linux/man-pages/man2/open.2.html) documentation for more details.

f

[openAsBlob](.././fs/~/openAsBlob "openAsBlob")

Returns a `Blob` whose data is backed by the given file.

f

[opendir](.././fs/~/opendir "opendir")

Asynchronously open a directory. See the POSIX [`opendir(3)`](http://man7.org/linux/man-pages/man3/opendir.3.html) documentation for more details.

f

[opendirSync](.././fs/~/opendirSync "opendirSync")

Synchronously open a directory. See [`opendir(3)`](http://man7.org/linux/man-pages/man3/opendir.3.html).

f

[openSync](.././fs/~/openSync "openSync")

Returns an integer representing the file descriptor.

f

[promises.access](.././fs/promises/~/promises.access "promises.access")

Tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g.`fs.constants.W_OK | fs.constants.R_OK`). Check `File access constants` for possible values of `mode`.

f

[promises.appendFile](.././fs/promises/~/promises.appendFile "promises.appendFile")

Asynchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `Buffer`.

f

[promises.chmod](.././fs/promises/~/promises.chmod "promises.chmod")

Changes the permissions of a file.

f

[promises.chown](.././fs/promises/~/promises.chown "promises.chown")

Changes the ownership of a file.

f

[promises.copyFile](.././fs/promises/~/promises.copyFile "promises.copyFile")

Asynchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists.

f

[promises.cp](.././fs/promises/~/promises.cp "promises.cp")

Asynchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.

f

[promises.glob](.././fs/promises/~/promises.glob "promises.glob")

Retrieves the files matching the specified pattern.

f

[promises.lchown](.././fs/promises/~/promises.lchown "promises.lchown")

Changes the ownership on a symbolic link.

f

[promises.link](.././fs/promises/~/promises.link "promises.link")

Creates a new link from the `existingPath` to the `newPath`. See the POSIX [`link(2)`](http://man7.org/linux/man-pages/man2/link.2.html) documentation for more detail.

f

[promises.lstat](.././fs/promises/~/promises.lstat "promises.lstat")

Equivalent to `fsPromises.stat()` unless `path` refers to a symbolic link, in which case the link itself is stat-ed, not the file that it refers to. Refer to the POSIX [`lstat(2)`](http://man7.org/linux/man-pages/man2/lstat.2.html) document for more detail.

f

[promises.lutimes](.././fs/promises/~/promises.lutimes "promises.lutimes")

Changes the access and modification times of a file in the same way as `fsPromises.utimes()`, with the difference that if the path refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link itself are changed.

f

[promises.mkdir](.././fs/promises/~/promises.mkdir "promises.mkdir")

Asynchronously creates a directory.

f

[promises.mkdtemp](.././fs/promises/~/promises.mkdtemp "promises.mkdtemp")

Creates a unique temporary directory. A unique directory name is generated by appending six random characters to the end of the provided `prefix`. Due to platform inconsistencies, avoid trailing `X` characters in `prefix`. Some platforms, notably the BSDs, can return more than six random characters, and replace trailing `X` characters in `prefix` with random characters.

f

[promises.open](.././fs/promises/~/promises.open "promises.open")

Opens a `FileHandle`.

f

[promises.opendir](.././fs/promises/~/promises.opendir "promises.opendir")

Asynchronously open a directory for iterative scanning. See the POSIX [`opendir(3)`](http://man7.org/linux/man-pages/man3/opendir.3.html) documentation for more detail.

f

[promises.readdir](.././fs/promises/~/promises.readdir "promises.readdir")

Reads the contents of a directory.

f

[promises.readFile](.././fs/promises/~/promises.readFile "promises.readFile")

Asynchronously reads the entire contents of a file.

f

[promises.readlink](.././fs/promises/~/promises.readlink "promises.readlink")

Reads the contents of the symbolic link referred to by `path`. See the POSIX [`readlink(2)`](http://man7.org/linux/man-pages/man2/readlink.2.html) documentation for more detail. The promise is fulfilled with the`linkString` upon success.

f

[promises.realpath](.././fs/promises/~/promises.realpath "promises.realpath")

Determines the actual location of `path` using the same semantics as the `fs.realpath.native()` function.

f

[promises.rename](.././fs/promises/~/promises.rename "promises.rename")

Renames `oldPath` to `newPath`.

f

[promises.rm](.././fs/promises/~/promises.rm "promises.rm")

Removes files and directories (modeled on the standard POSIX `rm` utility).

f

[promises.rmdir](.././fs/promises/~/promises.rmdir "promises.rmdir")

Removes the directory identified by `path`.

f

[promises.stat](.././fs/promises/~/promises.stat "promises.stat")

No documentation available

f

[promises.statfs](.././fs/promises/~/promises.statfs "promises.statfs")

No documentation available

f

[promises.symlink](.././fs/promises/~/promises.symlink "promises.symlink")

Creates a symbolic link.

f

[promises.truncate](.././fs/promises/~/promises.truncate "promises.truncate")

Truncates (shortens or extends the length) of the content at `path` to `len` bytes.

f

[promises.unlink](.././fs/promises/~/promises.unlink "promises.unlink")

If `path` refers to a symbolic link, then the link is removed without affecting the file or directory to which that link refers. If the `path` refers to a file path that is not a symbolic link, the file is deleted. See the POSIX [`unlink(2)`](http://man7.org/linux/man-pages/man2/unlink.2.html) documentation for more detail.

f

[promises.utimes](.././fs/promises/~/promises.utimes "promises.utimes")

Change the file system timestamps of the object referenced by `path`.

f

[promises.watch](.././fs/promises/~/promises.watch "promises.watch")

Returns an async iterator that watches for changes on `filename`, where `filename`is either a file or a directory.

f

[promises.writeFile](.././fs/promises/~/promises.writeFile "promises.writeFile")

Asynchronously writes data to a file, replacing the file if it already exists. `data` can be a string, a buffer, an [AsyncIterable](https://tc39.github.io/ecma262/#sec-asynciterable-interface), or an [Iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol) object.

f

[read](.././fs/~/read "read")

Read data from the file specified by `fd`.

f

[readdir](.././fs/~/readdir "readdir")

Reads the contents of a directory. The callback gets two arguments `(err, files)` where `files` is an array of the names of the files in the directory excluding `'.'` and `'..'`.

f

[readdirSync](.././fs/~/readdirSync "readdirSync")

Reads the contents of the directory.

f

[readFile](.././fs/~/readFile "readFile")

Asynchronously reads the entire contents of a file.

f

[readFileSync](.././fs/~/readFileSync "readFileSync")

Returns the contents of the `path`.

f

[readlink](.././fs/~/readlink "readlink")

Reads the contents of the symbolic link referred to by `path`. The callback gets two arguments `(err, linkString)`.

f

[readlinkSync](.././fs/~/readlinkSync "readlinkSync")

Returns the symbolic link's string value.

f

[readSync](.././fs/~/readSync "readSync")

Returns the number of `bytesRead`.

f

[readv](.././fs/~/readv "readv")

Read from a file specified by `fd` and write to an array of `ArrayBufferView`s using `readv()`.

f

[readvSync](.././fs/~/readvSync "readvSync")

For detailed information, see the documentation of the asynchronous version of this API: [readv](.././fs/~/readv).

f

N

[realpath](.././fs/~/realpath "realpath")

Asynchronously computes the canonical pathname by resolving `.`, `..`, and symbolic links.

f

[realpath.native](.././fs/~/realpath.native "realpath.native")

Asynchronous [`realpath(3)`](http://man7.org/linux/man-pages/man3/realpath.3.html).

f

N

[realpathSync](.././fs/~/realpathSync "realpathSync")

Returns the resolved pathname.

f

[realpathSync.native](.././fs/~/realpathSync.native "realpathSync.native")

No documentation available

f

[rename](.././fs/~/rename "rename")

Asynchronously rename file at `oldPath` to the pathname provided as `newPath`. In the case that `newPath` already exists, it will be overwritten. If there is a directory at `newPath`, an error will be raised instead. No arguments other than a possible exception are given to the completion callback.

f

[renameSync](.././fs/~/renameSync "renameSync")

Renames the file from `oldPath` to `newPath`. Returns `undefined`.

f

[rm](.././fs/~/rm "rm")

Asynchronously removes files and directories (modeled on the standard POSIX `rm` utility). No arguments other than a possible exception are given to the completion callback.

f

[rmdir](.././fs/~/rmdir "rmdir")

Asynchronous [`rmdir(2)`](http://man7.org/linux/man-pages/man2/rmdir.2.html). No arguments other than a possible exception are given to the completion callback.

f

[rmdirSync](.././fs/~/rmdirSync "rmdirSync")

Synchronous [`rmdir(2)`](http://man7.org/linux/man-pages/man2/rmdir.2.html). Returns `undefined`.

f

[rmSync](.././fs/~/rmSync "rmSync")

Synchronously removes files and directories (modeled on the standard POSIX `rm` utility). Returns `undefined`.

f

[stat](.././fs/~/stat "stat")

Asynchronous [`stat(2)`](http://man7.org/linux/man-pages/man2/stat.2.html). The callback gets two arguments `(err, stats)` where`stats` is an `fs.Stats` object.

f

[statfs](.././fs/~/statfs "statfs")

Asynchronous [`statfs(2)`](http://man7.org/linux/man-pages/man2/statfs.2.html). Returns information about the mounted file system which contains `path`. The callback gets two arguments `(err, stats)` where `stats`is an `fs.StatFs` object.

f

[statfsSync](.././fs/~/statfsSync "statfsSync")

Synchronous [`statfs(2)`](http://man7.org/linux/man-pages/man2/statfs.2.html). Returns information about the mounted file system which contains `path`.

f

N

[symlink](.././fs/~/symlink "symlink")

Creates the link called `path` pointing to `target`. No arguments other than a possible exception are given to the completion callback.

f

[symlinkSync](.././fs/~/symlinkSync "symlinkSync")

Returns `undefined`.

f

[truncate](.././fs/~/truncate "truncate")

Truncates the file. No arguments other than a possible exception are given to the completion callback. A file descriptor can also be passed as the first argument. In this case, `fs.ftruncate()` is called.

f

[truncateSync](.././fs/~/truncateSync "truncateSync")

Truncates the file. Returns `undefined`. A file descriptor can also be passed as the first argument. In this case, `fs.ftruncateSync()` is called.

f

[unlink](.././fs/~/unlink "unlink")

Asynchronously removes a file or symbolic link. No arguments other than a possible exception are given to the completion callback.

f

[unlinkSync](.././fs/~/unlinkSync "unlinkSync")

Synchronous [`unlink(2)`](http://man7.org/linux/man-pages/man2/unlink.2.html). Returns `undefined`.

f

[unwatchFile](.././fs/~/unwatchFile "unwatchFile")

Stop watching for changes on `filename`. If `listener` is specified, only that particular listener is removed. Otherwise, _all_ listeners are removed, effectively stopping watching of `filename`.

f

[utimes](.././fs/~/utimes "utimes")

Change the file system timestamps of the object referenced by `path`.

f

[utimesSync](.././fs/~/utimesSync "utimesSync")

Returns `undefined`.

f

[watch](.././fs/~/watch "watch")

Watch for changes on `filename`, where `filename` is either a file or a directory.

f

[watchFile](.././fs/~/watchFile "watchFile")

Watch for changes on `filename`. The callback `listener` will be called each time the file is accessed.

f

[write](.././fs/~/write "write")

Write `buffer` to the file specified by `fd`.

f

[writeFile](.././fs/~/writeFile "writeFile")

No documentation available

f

[writeFileSync](.././fs/~/writeFileSync "writeFileSync")

No documentation available

f

[writeSync](.././fs/~/writeSync "writeSync")

For detailed information, see the documentation of the asynchronous version of this API: [write](.././fs/~/write).

f

[writev](.././fs/~/writev "writev")

Write an array of `ArrayBufferView`s to the file specified by `fd` using `writev()`.

f

[writevSync](.././fs/~/writevSync "writevSync")

For detailed information, see the documentation of the asynchronous version of this API: [writev](.././fs/~/writev).

f

[exists](.././fs/~/exists "exists")

Test whether or not the given path exists by checking with the file system. Then call the `callback` argument with either true or false:

f

[lchmod](.././fs/~/lchmod "lchmod")

Changes the permissions on a symbolic link. No arguments other than a possible exception are given to the completion callback.

f

[lchmodSync](.././fs/~/lchmodSync "lchmodSync")

Changes the permissions on a symbolic link. Returns `undefined`.

f

[promises.lchmod](.././fs/promises/~/promises.lchmod "promises.lchmod")

No documentation available

I

[\_GlobOptions](.././fs/~/_GlobOptions "_GlobOptions")

No documentation available

-   [cwd](.././fs/~/_GlobOptions#property_cwd)
-   [exclude](.././fs/~/_GlobOptions#property_exclude)
-   [withFileTypes](.././fs/~/_GlobOptions#property_withfiletypes)

I

[BigIntOptions](.././fs/~/BigIntOptions "BigIntOptions")

No documentation available

-   [bigint](.././fs/~/BigIntOptions#property_bigint)

I

[BigIntStats](.././fs/~/BigIntStats "BigIntStats")

No documentation available

-   [atimeNs](.././fs/~/BigIntStats#property_atimens)
-   [birthtimeNs](.././fs/~/BigIntStats#property_birthtimens)
-   [ctimeNs](.././fs/~/BigIntStats#property_ctimens)
-   [mtimeNs](.././fs/~/BigIntStats#property_mtimens)

I

[BigIntStatsFs](.././fs/~/BigIntStatsFs "BigIntStatsFs")

No documentation available

I

[CopyOptions](.././fs/~/CopyOptions "CopyOptions")

No documentation available

-   [filter](.././fs/~/CopyOptions#method_filter_0)

I

[CopyOptionsBase](.././fs/~/CopyOptionsBase "CopyOptionsBase")

No documentation available

-   [dereference](.././fs/~/CopyOptionsBase#property_dereference)
-   [errorOnExist](.././fs/~/CopyOptionsBase#property_erroronexist)
-   [force](.././fs/~/CopyOptionsBase#property_force)
-   [mode](.././fs/~/CopyOptionsBase#property_mode)
-   [preserveTimestamps](.././fs/~/CopyOptionsBase#property_preservetimestamps)
-   [recursive](.././fs/~/CopyOptionsBase#property_recursive)
-   [verbatimSymlinks](.././fs/~/CopyOptionsBase#property_verbatimsymlinks)

I

[CopySyncOptions](.././fs/~/CopySyncOptions "CopySyncOptions")

No documentation available

-   [filter](.././fs/~/CopySyncOptions#method_filter_0)

I

[CreateReadStreamFSImplementation](.././fs/~/CreateReadStreamFSImplementation "CreateReadStreamFSImplementation")

No documentation available

-   [read](.././fs/~/CreateReadStreamFSImplementation#property_read)

I

[CreateWriteStreamFSImplementation](.././fs/~/CreateWriteStreamFSImplementation "CreateWriteStreamFSImplementation")

No documentation available

-   [write](.././fs/~/CreateWriteStreamFSImplementation#property_write)
-   [writev](.././fs/~/CreateWriteStreamFSImplementation#property_writev)

I

[FSImplementation](.././fs/~/FSImplementation "FSImplementation")

No documentation available

-   [close](.././fs/~/FSImplementation#property_close)
-   [open](.././fs/~/FSImplementation#property_open)

I

[FSWatcher](.././fs/~/FSWatcher "FSWatcher")

No documentation available

-   [addListener](.././fs/~/FSWatcher#method_addlistener_0)
-   [close](.././fs/~/FSWatcher#method_close_0)
-   [on](.././fs/~/FSWatcher#method_on_0)
-   [once](.././fs/~/FSWatcher#method_once_0)
-   [prependListener](.././fs/~/FSWatcher#method_prependlistener_0)
-   [prependOnceListener](.././fs/~/FSWatcher#method_prependoncelistener_0)
-   [ref](.././fs/~/FSWatcher#method_ref_0)
-   [unref](.././fs/~/FSWatcher#method_unref_0)

I

[GlobOptions](.././fs/~/GlobOptions "GlobOptions")

No documentation available

I

[GlobOptionsWithFileTypes](.././fs/~/GlobOptionsWithFileTypes "GlobOptionsWithFileTypes")

No documentation available

-   [withFileTypes](.././fs/~/GlobOptionsWithFileTypes#property_withfiletypes)

I

[GlobOptionsWithoutFileTypes](.././fs/~/GlobOptionsWithoutFileTypes "GlobOptionsWithoutFileTypes")

No documentation available

-   [withFileTypes](.././fs/~/GlobOptionsWithoutFileTypes#property_withfiletypes)

I

[MakeDirectoryOptions](.././fs/~/MakeDirectoryOptions "MakeDirectoryOptions")

No documentation available

-   [mode](.././fs/~/MakeDirectoryOptions#property_mode)
-   [recursive](.././fs/~/MakeDirectoryOptions#property_recursive)

I

[ObjectEncodingOptions](.././fs/~/ObjectEncodingOptions "ObjectEncodingOptions")

No documentation available

-   [encoding](.././fs/~/ObjectEncodingOptions#property_encoding)

I

[OpenAsBlobOptions](.././fs/~/OpenAsBlobOptions "OpenAsBlobOptions")

No documentation available

-   [type](.././fs/~/OpenAsBlobOptions#property_type)

I

[OpenDirOptions](.././fs/~/OpenDirOptions "OpenDirOptions")

No documentation available

-   [bufferSize](.././fs/~/OpenDirOptions#property_buffersize)
-   [encoding](.././fs/~/OpenDirOptions#property_encoding)
-   [recursive](.././fs/~/OpenDirOptions#property_recursive)

I

[promises.CreateReadStreamOptions](.././fs/promises/~/promises.CreateReadStreamOptions "promises.CreateReadStreamOptions")

No documentation available

-   [autoClose](.././fs/promises/~/promises.CreateReadStreamOptions#property_autoclose)
-   [emitClose](.././fs/promises/~/promises.CreateReadStreamOptions#property_emitclose)
-   [encoding](.././fs/promises/~/promises.CreateReadStreamOptions#property_encoding)
-   [end](.././fs/promises/~/promises.CreateReadStreamOptions#property_end)
-   [highWaterMark](.././fs/promises/~/promises.CreateReadStreamOptions#property_highwatermark)
-   [start](.././fs/promises/~/promises.CreateReadStreamOptions#property_start)

I

[promises.CreateWriteStreamOptions](.././fs/promises/~/promises.CreateWriteStreamOptions "promises.CreateWriteStreamOptions")

No documentation available

-   [autoClose](.././fs/promises/~/promises.CreateWriteStreamOptions#property_autoclose)
-   [emitClose](.././fs/promises/~/promises.CreateWriteStreamOptions#property_emitclose)
-   [encoding](.././fs/promises/~/promises.CreateWriteStreamOptions#property_encoding)
-   [flush](.././fs/promises/~/promises.CreateWriteStreamOptions#property_flush)
-   [highWaterMark](.././fs/promises/~/promises.CreateWriteStreamOptions#property_highwatermark)
-   [start](.././fs/promises/~/promises.CreateWriteStreamOptions#property_start)

I

[promises.FileChangeInfo](.././fs/promises/~/promises.FileChangeInfo "promises.FileChangeInfo")

No documentation available

-   [eventType](.././fs/promises/~/promises.FileChangeInfo#property_eventtype)
-   [filename](.././fs/promises/~/promises.FileChangeInfo#property_filename)

I

[promises.FileHandle](.././fs/promises/~/promises.FileHandle "promises.FileHandle")

No documentation available

-   [appendFile](.././fs/promises/~/promises.FileHandle#method_appendfile_0)
-   [chmod](.././fs/promises/~/promises.FileHandle#method_chmod_0)
-   [chown](.././fs/promises/~/promises.FileHandle#method_chown_0)
-   [close](.././fs/promises/~/promises.FileHandle#method_close_0)
-   [createReadStream](.././fs/promises/~/promises.FileHandle#method_createreadstream_0)
-   [createWriteStream](.././fs/promises/~/promises.FileHandle#method_createwritestream_0)
-   [datasync](.././fs/promises/~/promises.FileHandle#method_datasync_0)
-   [fd](.././fs/promises/~/promises.FileHandle#property_fd)
-   [read](.././fs/promises/~/promises.FileHandle#method_read_0)
-   [readFile](.././fs/promises/~/promises.FileHandle#method_readfile_0)
-   [readLines](.././fs/promises/~/promises.FileHandle#method_readlines_0)
-   [readableWebStream](.././fs/promises/~/promises.FileHandle#method_readablewebstream_0)
-   [readv](.././fs/promises/~/promises.FileHandle#method_readv_0)
-   [stat](.././fs/promises/~/promises.FileHandle#method_stat_0)
-   [sync](.././fs/promises/~/promises.FileHandle#method_sync_0)
-   [truncate](.././fs/promises/~/promises.FileHandle#method_truncate_0)
-   [utimes](.././fs/promises/~/promises.FileHandle#method_utimes_0)
-   [write](.././fs/promises/~/promises.FileHandle#method_write_0)
-   [writeFile](.././fs/promises/~/promises.FileHandle#method_writefile_0)
-   [writev](.././fs/promises/~/promises.FileHandle#method_writev_0)

I

[promises.FileReadOptions](.././fs/promises/~/promises.FileReadOptions "promises.FileReadOptions")

No documentation available

-   [buffer](.././fs/promises/~/promises.FileReadOptions#property_buffer)
-   [length](.././fs/promises/~/promises.FileReadOptions#property_length)
-   [offset](.././fs/promises/~/promises.FileReadOptions#property_offset)
-   [position](.././fs/promises/~/promises.FileReadOptions#property_position)

I

[promises.FileReadResult](.././fs/promises/~/promises.FileReadResult "promises.FileReadResult")

No documentation available

-   [buffer](.././fs/promises/~/promises.FileReadResult#property_buffer)
-   [bytesRead](.././fs/promises/~/promises.FileReadResult#property_bytesread)

I

[promises.FlagAndOpenMode](.././fs/promises/~/promises.FlagAndOpenMode "promises.FlagAndOpenMode")

No documentation available

-   [flag](.././fs/promises/~/promises.FlagAndOpenMode#property_flag)
-   [mode](.././fs/promises/~/promises.FlagAndOpenMode#property_mode)

I

[promises.ReadableWebStreamOptions](.././fs/promises/~/promises.ReadableWebStreamOptions "promises.ReadableWebStreamOptions")

No documentation available

-   [type](.././fs/promises/~/promises.ReadableWebStreamOptions#property_type)

I

[ReadAsyncOptions](.././fs/~/ReadAsyncOptions "ReadAsyncOptions")

No documentation available

-   [buffer](.././fs/~/ReadAsyncOptions#property_buffer)

I

[ReadStreamOptions](.././fs/~/ReadStreamOptions "ReadStreamOptions")

No documentation available

-   [end](.././fs/~/ReadStreamOptions#property_end)
-   [fs](.././fs/~/ReadStreamOptions#property_fs)

I

[ReadSyncOptions](.././fs/~/ReadSyncOptions "ReadSyncOptions")

No documentation available

-   [length](.././fs/~/ReadSyncOptions#property_length)
-   [offset](.././fs/~/ReadSyncOptions#property_offset)
-   [position](.././fs/~/ReadSyncOptions#property_position)

I

[ReadVResult](.././fs/~/ReadVResult "ReadVResult")

No documentation available

-   [buffers](.././fs/~/ReadVResult#property_buffers)
-   [bytesRead](.././fs/~/ReadVResult#property_bytesread)

I

[RmDirOptions](.././fs/~/RmDirOptions "RmDirOptions")

No documentation available

-   [maxRetries](.././fs/~/RmDirOptions#property_maxretries)
-   [recursive](.././fs/~/RmDirOptions#property_recursive)
-   [retryDelay](.././fs/~/RmDirOptions#property_retrydelay)

I

[RmOptions](.././fs/~/RmOptions "RmOptions")

No documentation available

-   [force](.././fs/~/RmOptions#property_force)
-   [maxRetries](.././fs/~/RmOptions#property_maxretries)
-   [recursive](.././fs/~/RmOptions#property_recursive)
-   [retryDelay](.././fs/~/RmOptions#property_retrydelay)

I

[StatFsOptions](.././fs/~/StatFsOptions "StatFsOptions")

No documentation available

-   [bigint](.././fs/~/StatFsOptions#property_bigint)

I

[StatOptions](.././fs/~/StatOptions "StatOptions")

No documentation available

-   [bigint](.././fs/~/StatOptions#property_bigint)

c

I

[Stats](.././fs/~/Stats "Stats")

A `fs.Stats` object provides information about a file.

I

[StatsBase](.././fs/~/StatsBase "StatsBase")

No documentation available

-   [atime](.././fs/~/StatsBase#property_atime)
-   [atimeMs](.././fs/~/StatsBase#property_atimems)
-   [birthtime](.././fs/~/StatsBase#property_birthtime)
-   [birthtimeMs](.././fs/~/StatsBase#property_birthtimems)
-   [blksize](.././fs/~/StatsBase#property_blksize)
-   [blocks](.././fs/~/StatsBase#property_blocks)
-   [ctime](.././fs/~/StatsBase#property_ctime)
-   [ctimeMs](.././fs/~/StatsBase#property_ctimems)
-   [dev](.././fs/~/StatsBase#property_dev)
-   [gid](.././fs/~/StatsBase#property_gid)
-   [ino](.././fs/~/StatsBase#property_ino)
-   [isBlockDevice](.././fs/~/StatsBase#method_isblockdevice_0)
-   [isCharacterDevice](.././fs/~/StatsBase#method_ischaracterdevice_0)
-   [isDirectory](.././fs/~/StatsBase#method_isdirectory_0)
-   [isFIFO](.././fs/~/StatsBase#method_isfifo_0)
-   [isFile](.././fs/~/StatsBase#method_isfile_0)
-   [isSocket](.././fs/~/StatsBase#method_issocket_0)
-   [isSymbolicLink](.././fs/~/StatsBase#method_issymboliclink_0)
-   [mode](.././fs/~/StatsBase#property_mode)
-   [mtime](.././fs/~/StatsBase#property_mtime)
-   [mtimeMs](.././fs/~/StatsBase#property_mtimems)
-   [nlink](.././fs/~/StatsBase#property_nlink)
-   [rdev](.././fs/~/StatsBase#property_rdev)
-   [size](.././fs/~/StatsBase#property_size)
-   [uid](.././fs/~/StatsBase#property_uid)

c

I

[StatsFs](.././fs/~/StatsFs "StatsFs")

Provides information about a mounted file system.

I

[StatsFsBase](.././fs/~/StatsFsBase "StatsFsBase")

No documentation available

-   [bavail](.././fs/~/StatsFsBase#property_bavail)
-   [bfree](.././fs/~/StatsFsBase#property_bfree)
-   [blocks](.././fs/~/StatsFsBase#property_blocks)
-   [bsize](.././fs/~/StatsFsBase#property_bsize)
-   [ffree](.././fs/~/StatsFsBase#property_ffree)
-   [files](.././fs/~/StatsFsBase#property_files)
-   [type](.././fs/~/StatsFsBase#property_type)

I

[StatSyncFn](.././fs/~/StatSyncFn "StatSyncFn")

No documentation available

I

[StatSyncOptions](.././fs/~/StatSyncOptions "StatSyncOptions")

No documentation available

-   [throwIfNoEntry](.././fs/~/StatSyncOptions#property_throwifnoentry)

I

[StatWatcher](.././fs/~/StatWatcher "StatWatcher")

Class: fs.StatWatcher

-   [ref](.././fs/~/StatWatcher#method_ref_0)
-   [unref](.././fs/~/StatWatcher#method_unref_0)

I

[StreamOptions](.././fs/~/StreamOptions "StreamOptions")

No documentation available

-   [autoClose](.././fs/~/StreamOptions#property_autoclose)
-   [emitClose](.././fs/~/StreamOptions#property_emitclose)
-   [encoding](.././fs/~/StreamOptions#property_encoding)
-   [fd](.././fs/~/StreamOptions#property_fd)
-   [flags](.././fs/~/StreamOptions#property_flags)
-   [highWaterMark](.././fs/~/StreamOptions#property_highwatermark)
-   [mode](.././fs/~/StreamOptions#property_mode)
-   [signal](.././fs/~/StreamOptions#property_signal)
-   [start](.././fs/~/StreamOptions#property_start)

I

[WatchFileOptions](.././fs/~/WatchFileOptions "WatchFileOptions")

Watch for changes on `filename`. The callback `listener` will be called each time the file is accessed.

-   [bigint](.././fs/~/WatchFileOptions#property_bigint)
-   [interval](.././fs/~/WatchFileOptions#property_interval)
-   [persistent](.././fs/~/WatchFileOptions#property_persistent)

I

[WatchOptions](.././fs/~/WatchOptions "WatchOptions")

No documentation available

-   [encoding](.././fs/~/WatchOptions#property_encoding)
-   [persistent](.././fs/~/WatchOptions#property_persistent)
-   [recursive](.././fs/~/WatchOptions#property_recursive)

I

[WriteStreamOptions](.././fs/~/WriteStreamOptions "WriteStreamOptions")

No documentation available

-   [flush](.././fs/~/WriteStreamOptions#property_flush)
-   [fs](.././fs/~/WriteStreamOptions#property_fs)

I

[WriteVResult](.././fs/~/WriteVResult "WriteVResult")

No documentation available

-   [buffers](.././fs/~/WriteVResult#property_buffers)
-   [bytesWritten](.././fs/~/WriteVResult#property_byteswritten)

N

[constants](.././fs/~/constants "constants")

No documentation available

N

[promises](.././fs/~/promises "promises")

The `fs/promises` API provides asynchronous file system methods that return promises.

T

[BigIntStatsListener](.././fs/~/BigIntStatsListener "BigIntStatsListener")

No documentation available

T

[BufferEncodingOption](.././fs/~/BufferEncodingOption "BufferEncodingOption")

No documentation available

T

[CustomEvents](.././fs/~/CustomEvents "CustomEvents")

string & {} allows to allow any kind of strings for the event but still allows to have auto completion for the normal events.

T

[EncodingOption](.././fs/~/EncodingOption "EncodingOption")

No documentation available

T

[Mode](.././fs/~/Mode "Mode")

No documentation available

T

[NoParamCallback](.././fs/~/NoParamCallback "NoParamCallback")

No documentation available

T

[OpenMode](.././fs/~/OpenMode "OpenMode")

No documentation available

T

[PathLike](.././fs/~/PathLike "PathLike")

Valid types for path values in "fs".

T

[PathOrFileDescriptor](.././fs/~/PathOrFileDescriptor "PathOrFileDescriptor")

No documentation available

T

[ReadPosition](.././fs/~/ReadPosition "ReadPosition")

No documentation available

T

[ReadStreamEvents](.././fs/~/ReadStreamEvents "ReadStreamEvents")

The Keys are events of the ReadStream and the values are the functions that are called when the event is emitted.

T

[StatsListener](.././fs/~/StatsListener "StatsListener")

No documentation available

T

[symlink.Type](.././fs/~/symlink.Type "symlink.Type")

No documentation available

T

[TimeLike](.././fs/~/TimeLike "TimeLike")

No documentation available

T

[WatchEventType](.././fs/~/WatchEventType "WatchEventType")

No documentation available

T

[WatchListener](.././fs/~/WatchListener "WatchListener")

No documentation available

T

[WriteFileOptions](.././fs/~/WriteFileOptions "WriteFileOptions")

No documentation available

T

[WriteStreamEvents](.././fs/~/WriteStreamEvents "WriteStreamEvents")

The Keys are events of the WriteStream and the values are the functions that are called when the event is emitted.

v

[constants.COPYFILE\_EXCL](.././fs/~/constants.COPYFILE_EXCL "constants.COPYFILE_EXCL")

Constant for fs.copyFile. Flag indicating the destination file should not be overwritten if it already exists.

v

[constants.COPYFILE\_FICLONE](.././fs/~/constants.COPYFILE_FICLONE "constants.COPYFILE_FICLONE")

Constant for fs.copyFile. copy operation will attempt to create a copy-on-write reflink. If the underlying platform does not support copy-on-write, then a fallback copy mechanism is used.

v

[constants.COPYFILE\_FICLONE\_FORCE](.././fs/~/constants.COPYFILE_FICLONE_FORCE "constants.COPYFILE_FICLONE_FORCE")

Constant for fs.copyFile. Copy operation will attempt to create a copy-on-write reflink. If the underlying platform does not support copy-on-write, then the operation will fail with an error.

v

[constants.F\_OK](.././fs/~/constants.F_OK "constants.F_OK")

Constant for fs.access(). File is visible to the calling process.

v

[constants.O\_APPEND](.././fs/~/constants.O_APPEND "constants.O_APPEND")

Constant for fs.open(). Flag indicating that data will be appended to the end of the file.

v

[constants.O\_CREAT](.././fs/~/constants.O_CREAT "constants.O_CREAT")

Constant for fs.open(). Flag indicating to create the file if it does not already exist.

v

[constants.O\_DIRECT](.././fs/~/constants.O_DIRECT "constants.O_DIRECT")

Constant for fs.open(). When set, an attempt will be made to minimize caching effects of file I/O.

v

[constants.O\_DIRECTORY](.././fs/~/constants.O_DIRECTORY "constants.O_DIRECTORY")

Constant for fs.open(). Flag indicating that the open should fail if the path is not a directory.

v

[constants.O\_DSYNC](.././fs/~/constants.O_DSYNC "constants.O_DSYNC")

Constant for fs.open(). Flag indicating that the file is opened for synchronous I/O with write operations waiting for data integrity.

v

[constants.O\_EXCL](.././fs/~/constants.O_EXCL "constants.O_EXCL")

Constant for fs.open(). Flag indicating that opening a file should fail if the O\_CREAT flag is set and the file already exists.

v

[constants.O\_NOATIME](.././fs/~/constants.O_NOATIME "constants.O_NOATIME")

constant for fs.open(). Flag indicating reading accesses to the file system will no longer result in an update to the atime information associated with the file. This flag is available on Linux operating systems only.

v

[constants.O\_NOCTTY](.././fs/~/constants.O_NOCTTY "constants.O_NOCTTY")

Constant for fs.open(). Flag indicating that if path identifies a terminal device, opening the path shall not cause that terminal to become the controlling terminal for the process (if the process does not already have one).

v

[constants.O\_NOFOLLOW](.././fs/~/constants.O_NOFOLLOW "constants.O_NOFOLLOW")

Constant for fs.open(). Flag indicating that the open should fail if the path is a symbolic link.

v

[constants.O\_NONBLOCK](.././fs/~/constants.O_NONBLOCK "constants.O_NONBLOCK")

Constant for fs.open(). Flag indicating to open the file in nonblocking mode when possible.

v

[constants.O\_RDONLY](.././fs/~/constants.O_RDONLY "constants.O_RDONLY")

Constant for fs.open(). Flag indicating to open a file for read-only access.

v

[constants.O\_RDWR](.././fs/~/constants.O_RDWR "constants.O_RDWR")

Constant for fs.open(). Flag indicating to open a file for read-write access.

v

[constants.O\_SYMLINK](.././fs/~/constants.O_SYMLINK "constants.O_SYMLINK")

Constant for fs.open(). Flag indicating to open the symbolic link itself rather than the resource it is pointing to.

v

[constants.O\_SYNC](.././fs/~/constants.O_SYNC "constants.O_SYNC")

Constant for fs.open(). Flag indicating that the file is opened for synchronous I/O.

v

[constants.O\_TRUNC](.././fs/~/constants.O_TRUNC "constants.O_TRUNC")

Constant for fs.open(). Flag indicating that if the file exists and is a regular file, and the file is opened successfully for write access, its length shall be truncated to zero.

v

[constants.O\_WRONLY](.././fs/~/constants.O_WRONLY "constants.O_WRONLY")

Constant for fs.open(). Flag indicating to open a file for write-only access.

v

[constants.R\_OK](.././fs/~/constants.R_OK "constants.R_OK")

Constant for fs.access(). File can be read by the calling process.

v

[constants.S\_IFBLK](.././fs/~/constants.S_IFBLK "constants.S_IFBLK")

Constant for fs.Stats mode property for determining a file's type. File type constant for a block-oriented device file.

v

[constants.S\_IFCHR](.././fs/~/constants.S_IFCHR "constants.S_IFCHR")

Constant for fs.Stats mode property for determining a file's type. File type constant for a character-oriented device file.

v

[constants.S\_IFDIR](.././fs/~/constants.S_IFDIR "constants.S_IFDIR")

Constant for fs.Stats mode property for determining a file's type. File type constant for a directory.

v

[constants.S\_IFIFO](.././fs/~/constants.S_IFIFO "constants.S_IFIFO")

Constant for fs.Stats mode property for determining a file's type. File type constant for a FIFO/pipe.

v

[constants.S\_IFLNK](.././fs/~/constants.S_IFLNK "constants.S_IFLNK")

Constant for fs.Stats mode property for determining a file's type. File type constant for a symbolic link.

v

[constants.S\_IFMT](.././fs/~/constants.S_IFMT "constants.S_IFMT")

Constant for fs.Stats mode property for determining a file's type. Bit mask used to extract the file type code.

v

[constants.S\_IFREG](.././fs/~/constants.S_IFREG "constants.S_IFREG")

Constant for fs.Stats mode property for determining a file's type. File type constant for a regular file.

v

[constants.S\_IFSOCK](.././fs/~/constants.S_IFSOCK "constants.S_IFSOCK")

Constant for fs.Stats mode property for determining a file's type. File type constant for a socket.

v

[constants.S\_IRGRP](.././fs/~/constants.S_IRGRP "constants.S_IRGRP")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable by group.

v

[constants.S\_IROTH](.././fs/~/constants.S_IROTH "constants.S_IROTH")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable by others.

v

[constants.S\_IRUSR](.././fs/~/constants.S_IRUSR "constants.S_IRUSR")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable by owner.

v

[constants.S\_IRWXG](.././fs/~/constants.S_IRWXG "constants.S_IRWXG")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable, writable and executable by group.

v

[constants.S\_IRWXO](.././fs/~/constants.S_IRWXO "constants.S_IRWXO")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable, writable and executable by others.

v

[constants.S\_IRWXU](.././fs/~/constants.S_IRWXU "constants.S_IRWXU")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable, writable and executable by owner.

v

[constants.S\_IWGRP](.././fs/~/constants.S_IWGRP "constants.S_IWGRP")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating writable by group.

v

[constants.S\_IWOTH](.././fs/~/constants.S_IWOTH "constants.S_IWOTH")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating writable by others.

v

[constants.S\_IWUSR](.././fs/~/constants.S_IWUSR "constants.S_IWUSR")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating writable by owner.

v

[constants.S\_IXGRP](.././fs/~/constants.S_IXGRP "constants.S_IXGRP")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating executable by group.

v

[constants.S\_IXOTH](.././fs/~/constants.S_IXOTH "constants.S_IXOTH")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating executable by others.

v

[constants.S\_IXUSR](.././fs/~/constants.S_IXUSR "constants.S_IXUSR")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating executable by owner.

v

[constants.UV\_FS\_O\_FILEMAP](.././fs/~/constants.UV_FS_O_FILEMAP "constants.UV_FS_O_FILEMAP")

When set, a memory file mapping is used to access the file. This flag is available on Windows operating systems only. On other operating systems, this flag is ignored.

v

[constants.W\_OK](.././fs/~/constants.W_OK "constants.W_OK")

Constant for fs.access(). File can be written by the calling process.

v

[constants.X\_OK](.././fs/~/constants.X_OK "constants.X_OK")

Constant for fs.access(). File can be executed by the calling process.

v

[lstatSync](.././fs/~/lstatSync "lstatSync")

Synchronous lstat(2) - Get file status. Does not dereference symbolic links.

v

[promises.constants](.././fs/promises/~/promises.constants "promises.constants")

No documentation available

v

[statSync](.././fs/~/statSync "statSync")

Synchronous stat(2) - Get file status.
