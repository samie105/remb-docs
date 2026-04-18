---
title: "File System - Deno documentation"
source: "https://docs.deno.com/api/deno/file-system"
canonical_url: "https://docs.deno.com/api/deno/file-system"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:09:20.575Z"
content_hash: "f6b7b4ed650d7ebec257bb6351fe60132f78684a17bfbecc7ff47ad68742249c"
menu_path: ["File System - Deno documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/deno/ffi/index.md", "title": "FFI - Deno documentation"}
nav_next: {"path": "deno/deno/api/deno/gpu/index.md", "title": "GPU - Deno documentation"}
---

### Classes [#](#Classes)

c

[Deno.FsFile](./././~/Deno.FsFile "Deno.FsFile")

The Deno abstraction for reading and writing files.

*   [close](./././~/Deno.FsFile#method_close_0)
*   [isTerminal](./././~/Deno.FsFile#method_isterminal_0)
*   [lock](./././~/Deno.FsFile#method_lock_0)
*   [lockSync](./././~/Deno.FsFile#method_locksync_0)
*   [read](./././~/Deno.FsFile#method_read_0)
*   [readSync](./././~/Deno.FsFile#method_readsync_0)
*   [readable](./././~/Deno.FsFile#property_readable)
*   [seek](./././~/Deno.FsFile#method_seek_0)
*   [seekSync](./././~/Deno.FsFile#method_seeksync_0)
*   [setRaw](./././~/Deno.FsFile#method_setraw_0)
*   [stat](./././~/Deno.FsFile#method_stat_0)
*   [statSync](./././~/Deno.FsFile#method_statsync_0)
*   [sync](./././~/Deno.FsFile#method_sync_0)
*   [syncData](./././~/Deno.FsFile#method_syncdata_0)
*   [syncDataSync](./././~/Deno.FsFile#method_syncdatasync_0)
*   [syncSync](./././~/Deno.FsFile#method_syncsync_0)
*   [truncate](./././~/Deno.FsFile#method_truncate_0)
*   [truncateSync](./././~/Deno.FsFile#method_truncatesync_0)
*   [tryLock](./././~/Deno.FsFile#method_trylock_0)
*   [tryLockSync](./././~/Deno.FsFile#method_trylocksync_0)
*   [unlock](./././~/Deno.FsFile#method_unlock_0)
*   [unlockSync](./././~/Deno.FsFile#method_unlocksync_0)
*   [utime](./././~/Deno.FsFile#method_utime_0)
*   [utimeSync](./././~/Deno.FsFile#method_utimesync_0)
*   [writable](./././~/Deno.FsFile#property_writable)
*   [write](./././~/Deno.FsFile#method_write_0)
*   [writeSync](./././~/Deno.FsFile#method_writesync_0)

### Functions [#](#Functions)

f

[Deno.chmod](./././~/Deno.chmod "Deno.chmod")

Changes the permission of a specific file/directory of specified path. Ignores the process's umask.

f

[Deno.chmodSync](./././~/Deno.chmodSync "Deno.chmodSync")

Synchronously changes the permission of a specific file/directory of specified path. Ignores the process's umask.

f

[Deno.chown](./././~/Deno.chown "Deno.chown")

Change owner of a regular file or directory.

f

[Deno.chownSync](./././~/Deno.chownSync "Deno.chownSync")

Synchronously change owner of a regular file or directory.

f

[Deno.copyFile](./././~/Deno.copyFile "Deno.copyFile")

Copies the contents and permissions of one file to another specified path, by default creating a new file if needed, else overwriting. Fails if target path is a directory or is unwritable.

f

[Deno.copyFileSync](./././~/Deno.copyFileSync "Deno.copyFileSync")

Synchronously copies the contents and permissions of one file to another specified path, by default creating a new file if needed, else overwriting. Fails if target path is a directory or is unwritable.

f

[Deno.create](./././~/Deno.create "Deno.create")

Creates a file if none exists or truncates an existing file and resolves to an instance of [`Deno.FsFile`](./././~/Deno.FsFile).

f

[Deno.createSync](./././~/Deno.createSync "Deno.createSync")

Creates a file if none exists or truncates an existing file and returns an instance of [`Deno.FsFile`](./././~/Deno.FsFile).

f

[Deno.link](./././~/Deno.link "Deno.link")

Creates `newpath` as a hard link to `oldpath`.

f

[Deno.linkSync](./././~/Deno.linkSync "Deno.linkSync")

Synchronously creates `newpath` as a hard link to `oldpath`.

f

[Deno.lstat](./././~/Deno.lstat "Deno.lstat")

Resolves to a [`Deno.FileInfo`](./././~/Deno.FileInfo) for the specified `path`. If `path` is a symlink, information for the symlink will be returned instead of what it points to.

f

[Deno.lstatSync](./././~/Deno.lstatSync "Deno.lstatSync")

Synchronously returns a [`Deno.FileInfo`](./././~/Deno.FileInfo) for the specified `path`. If `path` is a symlink, information for the symlink will be returned instead of what it points to.

f

[Deno.makeTempDir](./././~/Deno.makeTempDir "Deno.makeTempDir")

Creates a new temporary directory in the default directory for temporary files, unless `dir` is specified. Other optional options include prefixing and suffixing the directory name with `prefix` and `suffix` respectively.

f

[Deno.makeTempDirSync](./././~/Deno.makeTempDirSync "Deno.makeTempDirSync")

Synchronously creates a new temporary directory in the default directory for temporary files, unless `dir` is specified. Other optional options include prefixing and suffixing the directory name with `prefix` and `suffix` respectively.

f

[Deno.makeTempFile](./././~/Deno.makeTempFile "Deno.makeTempFile")

Creates a new temporary file in the default directory for temporary files, unless `dir` is specified.

f

[Deno.makeTempFileSync](./././~/Deno.makeTempFileSync "Deno.makeTempFileSync")

Synchronously creates a new temporary file in the default directory for temporary files, unless `dir` is specified.

f

[Deno.mkdir](./././~/Deno.mkdir "Deno.mkdir")

Creates a new directory with the specified path.

f

[Deno.mkdirSync](./././~/Deno.mkdirSync "Deno.mkdirSync")

Synchronously creates a new directory with the specified path.

f

[Deno.open](./././~/Deno.open "Deno.open")

Open a file and resolve to an instance of [`Deno.FsFile`](./././~/Deno.FsFile). The file does not need to previously exist if using the `create` or `createNew` open options. The caller may have the resulting file automatically closed by the runtime once it's out of scope by declaring the file variable with the `using` keyword.

f

[Deno.openSync](./././~/Deno.openSync "Deno.openSync")

Synchronously open a file and return an instance of [`Deno.FsFile`](./././~/Deno.FsFile). The file does not need to previously exist if using the `create` or `createNew` open options. The caller may have the resulting file automatically closed by the runtime once it's out of scope by declaring the file variable with the `using` keyword.

f

[Deno.readDir](./././~/Deno.readDir "Deno.readDir")

Reads the directory given by `path` and returns an async iterable of [`Deno.DirEntry`](./././~/Deno.DirEntry). The order of entries is not guaranteed.

f

[Deno.readDirSync](./././~/Deno.readDirSync "Deno.readDirSync")

Synchronously reads the directory given by `path` and returns an iterable of [`Deno.DirEntry`](./././~/Deno.DirEntry). The order of entries is not guaranteed.

f

[Deno.readFile](./././~/Deno.readFile "Deno.readFile")

Reads and resolves to the entire contents of a file as an array of bytes. `TextDecoder` can be used to transform the bytes to string if required. Rejects with an error when reading a directory.

f

[Deno.readFileSync](./././~/Deno.readFileSync "Deno.readFileSync")

Synchronously reads and returns the entire contents of a file as an array of bytes. `TextDecoder` can be used to transform the bytes to string if required. Throws an error when reading a directory.

f

[Deno.readLink](./././~/Deno.readLink "Deno.readLink")

Resolves to the full path destination of the named symbolic link.

f

[Deno.readLinkSync](./././~/Deno.readLinkSync "Deno.readLinkSync")

Synchronously returns the full path destination of the named symbolic link.

f

[Deno.readTextFile](./././~/Deno.readTextFile "Deno.readTextFile")

Asynchronously reads and returns the entire contents of a file as an UTF-8 decoded string. Reading a directory throws an error.

f

[Deno.readTextFileSync](./././~/Deno.readTextFileSync "Deno.readTextFileSync")

Synchronously reads and returns the entire contents of a file as an UTF-8 decoded string. Reading a directory throws an error.

f

[Deno.realPath](./././~/Deno.realPath "Deno.realPath")

Resolves to the absolute normalized path, with symbolic links resolved.

f

[Deno.realPathSync](./././~/Deno.realPathSync "Deno.realPathSync")

Synchronously returns absolute normalized path, with symbolic links resolved.

f

[Deno.remove](./././~/Deno.remove "Deno.remove")

Removes the named file or directory.

f

[Deno.removeSync](./././~/Deno.removeSync "Deno.removeSync")

Synchronously removes the named file or directory.

f

[Deno.rename](./././~/Deno.rename "Deno.rename")

Renames (moves) `oldpath` to `newpath`. Paths may be files or directories. If `newpath` already exists and is not a directory, `rename()` replaces it. OS-specific restrictions may apply when `oldpath` and `newpath` are in different directories.

f

[Deno.renameSync](./././~/Deno.renameSync "Deno.renameSync")

Synchronously renames (moves) `oldpath` to `newpath`. Paths may be files or directories. If `newpath` already exists and is not a directory, `renameSync()` replaces it. OS-specific restrictions may apply when `oldpath` and `newpath` are in different directories.

f

[Deno.stat](./././~/Deno.stat "Deno.stat")

Resolves to a [`Deno.FileInfo`](./././~/Deno.FileInfo) for the specified `path`. Will always follow symlinks.

f

[Deno.statSync](./././~/Deno.statSync "Deno.statSync")

Synchronously returns a [`Deno.FileInfo`](./././~/Deno.FileInfo) for the specified `path`. Will always follow symlinks.

f

[Deno.symlink](./././~/Deno.symlink "Deno.symlink")

Creates `newpath` as a symbolic link to `oldpath`.

f

[Deno.symlinkSync](./././~/Deno.symlinkSync "Deno.symlinkSync")

Creates `newpath` as a symbolic link to `oldpath`.

f

[Deno.truncate](./././~/Deno.truncate "Deno.truncate")

Truncates (or extends) the specified file, to reach the specified `len`. If `len` is not specified then the entire file contents are truncated.

f

[Deno.truncateSync](./././~/Deno.truncateSync "Deno.truncateSync")

Synchronously truncates (or extends) the specified file, to reach the specified `len`. If `len` is not specified then the entire file contents are truncated.

f

[Deno.umask](./././~/Deno.umask "Deno.umask")

Retrieve the process umask. If `mask` is provided, sets the process umask. This call always returns what the umask was before the call.

f

[Deno.utime](./././~/Deno.utime "Deno.utime")

Changes the access (`atime`) and modification (`mtime`) times of a file system object referenced by `path`. Given times are either in seconds (UNIX epoch time) or as `Date` objects.

f

[Deno.utimeSync](./././~/Deno.utimeSync "Deno.utimeSync")

Synchronously changes the access (`atime`) and modification (`mtime`) times of a file system object referenced by `path`. Given times are either in seconds (UNIX epoch time) or as `Date` objects.

f

[Deno.watchFs](./././~/Deno.watchFs "Deno.watchFs")

Watch for file system events against one or more `paths`, which can be files or directories. These paths must exist already. One user action (e.g. `touch test.file`) can generate multiple file system events. Likewise, one user action can result in multiple file paths in one event (e.g. `mv old_name.txt new_name.txt`).

f

[Deno.writeFile](./././~/Deno.writeFile "Deno.writeFile")

Write `data` to the given `path`, by default creating a new file if needed, else overwriting.

f

[Deno.writeFileSync](./././~/Deno.writeFileSync "Deno.writeFileSync")

Synchronously write `data` to the given `path`, by default creating a new file if needed, else overwriting.

f

[Deno.writeTextFile](./././~/Deno.writeTextFile "Deno.writeTextFile")

Write string `data` to the given `path`, by default creating a new file if needed, else overwriting.

f

[Deno.writeTextFileSync](./././~/Deno.writeTextFileSync "Deno.writeTextFileSync")

Synchronously write string `data` to the given `path`, by default creating a new file if needed, else overwriting.

### Interfaces [#](#Interfaces)

I

[Deno.DirEntry](./././~/Deno.DirEntry "Deno.DirEntry")

Information about a directory entry returned from [`Deno.readDir`](./././~/Deno.readDir) and [`Deno.readDirSync`](./././~/Deno.readDirSync).

*   [isDirectory](./././~/Deno.DirEntry#property_isdirectory)
*   [isFile](./././~/Deno.DirEntry#property_isfile)
*   [isSymlink](./././~/Deno.DirEntry#property_issymlink)
*   [name](./././~/Deno.DirEntry#property_name)

I

[Deno.FileInfo](./././~/Deno.FileInfo "Deno.FileInfo")

Provides information about a file and is returned by [`Deno.stat`](./././~/Deno.stat), [`Deno.lstat`](./././~/Deno.lstat), [`Deno.statSync`](./././~/Deno.statSync), and [`Deno.lstatSync`](./././~/Deno.lstatSync) or from calling `stat()` and `statSync()` on an [`Deno.FsFile`](./././~/Deno.FsFile) instance.

*   [atime](./././~/Deno.FileInfo#property_atime)
*   [birthtime](./././~/Deno.FileInfo#property_birthtime)
*   [blksize](./././~/Deno.FileInfo#property_blksize)
*   [blocks](./././~/Deno.FileInfo#property_blocks)
*   [ctime](./././~/Deno.FileInfo#property_ctime)
*   [dev](./././~/Deno.FileInfo#property_dev)
*   [gid](./././~/Deno.FileInfo#property_gid)
*   [ino](./././~/Deno.FileInfo#property_ino)
*   [isBlockDevice](./././~/Deno.FileInfo#property_isblockdevice)
*   [isCharDevice](./././~/Deno.FileInfo#property_ischardevice)
*   [isDirectory](./././~/Deno.FileInfo#property_isdirectory)
*   [isFifo](./././~/Deno.FileInfo#property_isfifo)
*   [isFile](./././~/Deno.FileInfo#property_isfile)
*   [isSocket](./././~/Deno.FileInfo#property_issocket)
*   [isSymlink](./././~/Deno.FileInfo#property_issymlink)
*   [mode](./././~/Deno.FileInfo#property_mode)
*   [mtime](./././~/Deno.FileInfo#property_mtime)
*   [nlink](./././~/Deno.FileInfo#property_nlink)
*   [rdev](./././~/Deno.FileInfo#property_rdev)
*   [size](./././~/Deno.FileInfo#property_size)
*   [uid](./././~/Deno.FileInfo#property_uid)

I

[Deno.FsEvent](./././~/Deno.FsEvent "Deno.FsEvent")

Represents a unique file system event yielded by a [`Deno.FsWatcher`](./././~/Deno.FsWatcher).

*   [flag](./././~/Deno.FsEvent#property_flag)
*   [kind](./././~/Deno.FsEvent#property_kind)
*   [paths](./././~/Deno.FsEvent#property_paths)

I

[Deno.FsWatcher](./././~/Deno.FsWatcher "Deno.FsWatcher")

Returned by [`Deno.watchFs`](./././~/Deno.watchFs). It is an async iterator yielding up system events. To stop watching the file system by calling `.close()` method.

*   [close](./././~/Deno.FsWatcher#method_close_0)
*   [return](./././~/Deno.FsWatcher#method_return_0)

I

[Deno.MakeTempOptions](./././~/Deno.MakeTempOptions "Deno.MakeTempOptions")

Options which can be set when using [`Deno.makeTempDir`](./././~/Deno.makeTempDir), [`Deno.makeTempDirSync`](./././~/Deno.makeTempDirSync), [`Deno.makeTempFile`](./././~/Deno.makeTempFile), and [`Deno.makeTempFileSync`](./././~/Deno.makeTempFileSync).

*   [dir](./././~/Deno.MakeTempOptions#property_dir)
*   [prefix](./././~/Deno.MakeTempOptions#property_prefix)
*   [suffix](./././~/Deno.MakeTempOptions#property_suffix)

I

[Deno.MkdirOptions](./././~/Deno.MkdirOptions "Deno.MkdirOptions")

Options which can be set when using [`Deno.mkdir`](./././~/Deno.mkdir) and [`Deno.mkdirSync`](./././~/Deno.mkdirSync).

*   [mode](./././~/Deno.MkdirOptions#property_mode)
*   [recursive](./././~/Deno.MkdirOptions#property_recursive)

I

[Deno.OpenOptions](./././~/Deno.OpenOptions "Deno.OpenOptions")

Options which can be set when doing [`Deno.open`](./././~/Deno.open) and [`Deno.openSync`](./././~/Deno.openSync).

*   [append](./././~/Deno.OpenOptions#property_append)
*   [create](./././~/Deno.OpenOptions#property_create)
*   [createNew](./././~/Deno.OpenOptions#property_createnew)
*   [mode](./././~/Deno.OpenOptions#property_mode)
*   [read](./././~/Deno.OpenOptions#property_read)
*   [truncate](./././~/Deno.OpenOptions#property_truncate)
*   [write](./././~/Deno.OpenOptions#property_write)

I

[Deno.ReadFileOptions](./././~/Deno.ReadFileOptions "Deno.ReadFileOptions")

Options which can be set when using [`Deno.readFile`](./././~/Deno.readFile) or [`Deno.readFileSync`](./././~/Deno.readFileSync).

*   [signal](./././~/Deno.ReadFileOptions#property_signal)

I

[Deno.RemoveOptions](./././~/Deno.RemoveOptions "Deno.RemoveOptions")

Options which can be set when using [`Deno.remove`](./././~/Deno.remove) and [`Deno.removeSync`](./././~/Deno.removeSync).

*   [recursive](./././~/Deno.RemoveOptions#property_recursive)

I

[Deno.SymlinkOptions](./././~/Deno.SymlinkOptions "Deno.SymlinkOptions")

Options that can be used with `symlink` and `symlinkSync`.

*   [type](./././~/Deno.SymlinkOptions#property_type)

I

[Deno.WriteFileOptions](./././~/Deno.WriteFileOptions "Deno.WriteFileOptions")

Options for writing to a file.

*   [append](./././~/Deno.WriteFileOptions#property_append)
*   [create](./././~/Deno.WriteFileOptions#property_create)
*   [createNew](./././~/Deno.WriteFileOptions#property_createnew)
*   [mode](./././~/Deno.WriteFileOptions#property_mode)
*   [signal](./././~/Deno.WriteFileOptions#property_signal)

### Type Aliases [#](<#Type Aliases>)

T

[Deno.FsEventFlag](./././~/Deno.FsEventFlag "Deno.FsEventFlag")

Additional information for FsEvent objects with the "other" kind.


