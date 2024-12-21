import regex
import pandas as pd
import numpy as np
import tempfile
import os
import subprocess
from touchtouch import touch

importstoadd = """from libc.stdint cimport *
from libcpp.vector cimport vector
from libcpp.utility cimport pair
from libcpp.random cimport random_device
from libcpp.random cimport mt19937
from libcpp.random cimport mt19937_64
from libcpp.map cimport map as cpp_map
from libcpp.map cimport multimap
from libcpp.complex cimport complex as cpp_complex
from libcpp.unordered_set cimport unordered_set
from libcpp.unordered_set cimport unordered_multiset
from libcpp.queue cimport queue as cpp_queue
from libcpp.queue cimport priority_queue
from libcpp.list cimport list as cpp_list
from libcpp.atomic cimport atomic
from libcpp.optional cimport nullopt_t
from libcpp.optional cimport optional
from libcpp.memory cimport default_delete
from libcpp.memory cimport allocator
from libcpp.memory cimport unique_ptr
from libcpp.memory cimport shared_ptr
from libcpp.memory cimport weak_ptr
from libcpp.forward_list cimport forward_list
from libcpp.unordered_map cimport unordered_map
from libcpp.unordered_map cimport unordered_multimap
from libcpp.limits cimport numeric_limits
from libcpp.any cimport any as cpp_any
from libcpp.deque cimport deque as cpp_deque
from libcpp.set cimport set as cpp_set
from libcpp.set cimport multiset
from libcpp.typeinfo cimport type_info
from libcpp.stack cimport stack
from libcpp.functional cimport function
from libcpp.functional cimport greater
from libcpp.functional cimport reference_wrapper
from libcpp.string cimport string
from libcpp.typeindex cimport type_index
from cython cimport sizeof
from libc.stddef import * """

windtypes = """
# Define fundamental types
ctypedef int8_t CHAR
ctypedef uint8_t BYTE
ctypedef int32_t BOOL
ctypedef int32_t LONG
ctypedef uint32_t DWORD
ctypedef int32_t INT
ctypedef uint32_t UINT
ctypedef int16_t SHORT
ctypedef uint16_t USHORT
ctypedef uint16_t WORD
ctypedef int64_t LONGLONG
ctypedef uint64_t ULONGLONG
ctypedef float FLOAT
ctypedef double DOUBLE

ctypedef BOOL *LPBOOL
ctypedef BYTE *LPBYTE
ctypedef BYTE *PBYTE
ctypedef BOOL *PBOOL
ctypedef BYTE BOOLEAN
ctypedef BOOLEAN *PBOOLEAN
ctypedef CHAR *PCHAR

ctypedef WCHAR wchar_t
ctypedef WCHAR *PWCHAR
ctypedef WCHAR *LPWSTR
ctypedef const WCHAR *LPCWSTR
ctypedef CHAR *LPSTR
ctypedef const CHAR *LPCSTR
ctypedef void *LPVOID
ctypedef const void *LPCVOID

ctypedef WCHAR *LPOLESTR
ctypedef const WCHAR *LPCOLESTR
ctypedef WCHAR *OLESTR

ctypedef uint64_t ULONG64
ctypedef uint64_t DWORD64
ctypedef int64_t LONG64
ctypedef int64_t INT64

ctypedef ULONG64 *PULONG64
ctypedef DWORD64 *PDWORD64
ctypedef LONG64 *PLONG64
ctypedef INT64 *PINT64

ctypedef uint32_t ULONG
ctypedef int32_t LONG32
ctypedef uint32_t DWORD32
ctypedef int32_t INT32

ctypedef ULONG *PULONG
ctypedef LONG32 *PLONG32
ctypedef DWORD32 *PDWORD32
ctypedef INT32 *PINT32

ctypedef uint16_t UINT16
ctypedef int16_t INT16
ctypedef UINT16 *PUINT16
ctypedef INT16 *PINT16

ctypedef uint8_t UINT8
ctypedef int8_t INT8
ctypedef UINT8 *PUINT8
ctypedef INT8 *PINT8

ctypedef FLOAT *PFLOAT
ctypedef DOUBLE *PDOUBLE

ctypedef WORD *LPWORD
ctypedef WORD *PWORD
ctypedef DWORD *LPDWORD
ctypedef DWORD *PDWORD
ctypedef LONG *LPLONG
ctypedef LONG *PLONG
ctypedef INT *LPINT
ctypedef INT *PINT
ctypedef UINT *LPUINT
ctypedef UINT *PUINT
ctypedef SHORT *PSHORT
ctypedef USHORT *PUSHORT
ctypedef ULONG *PULONG
ctypedef WCHAR *PWCHAR

ctypedef uint64_t QWORD

ctypedef int64_t INT_PTR
ctypedef int64_t LONG_PTR
ctypedef uint64_t UINT_PTR
ctypedef uint64_t ULONG_PTR
ctypedef int64_t LPARAM
ctypedef uint64_t WPARAM
ctypedef int64_t SSIZE_T
ctypedef uint64_t SIZE_T

ctypedef ULONG_PTR DWORD_PTR
ctypedef ULONG_PTR *PULONG_PTR
ctypedef LONG_PTR *PLONG_PTR
ctypedef INT_PTR *PINT_PTR
ctypedef UINT_PTR *PUINT_PTR

# Handle types
ctypedef void *HANDLE
ctypedef HANDLE *LPHANDLE
ctypedef HANDLE *PHANDLE

ctypedef HANDLE HACCEL
ctypedef HANDLE HBITMAP
ctypedef HANDLE HBRUSH
ctypedef HANDLE HCOLORSPACE
ctypedef HANDLE HCONV
ctypedef HANDLE HCONVLIST
ctypedef HANDLE HDC
ctypedef HANDLE HDDEDATA
ctypedef HANDLE HDESK
ctypedef HANDLE HDROP
ctypedef HANDLE HDWP
ctypedef HANDLE HENHMETAFILE
ctypedef HANDLE HFONT
ctypedef HANDLE HGDIOBJ
ctypedef HANDLE HGLOBAL
ctypedef HANDLE HHOOK
ctypedef HANDLE HICON
ctypedef HANDLE HINSTANCE
ctypedef HANDLE HKEY
ctypedef HANDLE HKL
ctypedef HANDLE HLOCAL
ctypedef HANDLE HMENU
ctypedef HANDLE HMETAFILE
ctypedef HANDLE HMODULE
ctypedef HANDLE HMONITOR
ctypedef HANDLE HPALETTE
ctypedef HANDLE HPEN
ctypedef HANDLE HRGN
ctypedef HANDLE HRSRC
ctypedef HANDLE HSTR
ctypedef HANDLE HTASK
ctypedef HANDLE HWINSTA
ctypedef HANDLE HWND
ctypedef HANDLE SC_HANDLE
ctypedef HANDLE SERVICE_STATUS_HANDLE

ctypedef HINSTANCE HMODULE
ctypedef HICON HCURSOR

ctypedef HANDLE *PHKEY
ctypedef HANDLE *PHKL

# Additional typedefs
ctypedef WORD ATOM
ctypedef WORD LANGID

ctypedef DWORD COLORREF
ctypedef DWORD LCTYPE
ctypedef DWORD LGRPID
ctypedef DWORD LCID
ctypedef DWORD *LPCOLORREF
ctypedef LCID *PLCID

ctypedef uint16_t USHORT
ctypedef int16_t SHORT
ctypedef SHORT *PSHORT

# Define MAX_PATH
cdef int MAX_PATH = 260

# Structures
cdef struct RECT:
    LONG left
    LONG top
    LONG right
    LONG bottom

ctypedef RECT *LPRECT
ctypedef RECT *PRECT

cdef struct POINT:
    LONG x
    LONG y

ctypedef POINT *LPPOINT
ctypedef POINT *PPOINT

cdef struct SIZE:
    LONG cx
    LONG cy

ctypedef SIZE *LPSIZE
ctypedef SIZE *PSIZE

cdef struct FILETIME:
    DWORD dwLowDateTime
    DWORD dwHighDateTime

ctypedef FILETIME *LPFILETIME
ctypedef FILETIME *PFILETIME

cdef struct MSG:
    HWND hWnd
    UINT message
    WPARAM wParam
    LPARAM lParam
    DWORD time
    POINT pt

ctypedef MSG *LPMSG
ctypedef MSG *PMSG

cdef struct COORD:
    SHORT X
    SHORT Y

ctypedef COORD *PCOORD

cdef struct SMALL_RECT:
    SHORT Left
    SHORT Top
    SHORT Right
    SHORT Bottom

ctypedef SMALL_RECT *PSMALL_RECT

cdef struct WIN32_FIND_DATAA:
    DWORD dwFileAttributes
    FILETIME ftCreationTime
    FILETIME ftLastAccessTime
    FILETIME ftLastWriteTime
    DWORD nFileSizeHigh
    DWORD nFileSizeLow
    DWORD dwReserved0
    DWORD dwReserved1
    CHAR cFileName[MAX_PATH]
    CHAR cAlternateFileName[14]

ctypedef WIN32_FIND_DATAA *LPWIN32_FIND_DATAA
ctypedef WIN32_FIND_DATAA *PWIN32_FIND_DATAA

cdef struct WIN32_FIND_DATAW:
    DWORD dwFileAttributes
    FILETIME ftCreationTime
    FILETIME ftLastAccessTime
    FILETIME ftLastWriteTime
    DWORD nFileSizeHigh
    DWORD nFileSizeLow
    DWORD dwReserved0
    DWORD dwReserved1
    WCHAR[MAX_PATH] cFileName
    WCHAR[14] cAlternateFileName

ctypedef WIN32_FIND_DATAW *LPWIN32_FIND_DATAW
ctypedef WIN32_FIND_DATAW *PWIN32_FIND_DATAW
ctypedef LARGE_INTEGER longlong 
ctypedef _LARGE_INTEGER LARGE_INTEGER
ctypedef ULARGE_INTEGER ulonglong 
ctypedef _ULARGE_INTEGER ULARGE_INTEGER 

# VARIANT_BOOL
ctypedef int16_t VARIANT_BOOL

# Additional pointer types
ctypedef PVOID LPCVOID
ctypedef CHAR *PSTR
ctypedef WCHAR *PWSTR
ctypedef const CHAR *PCSTR
ctypedef const WCHAR *PCWSTR

ctypedef HANDLE *PHANDLE
ctypedef HKEY *PHKEY
ctypedef HINSTANCE *PHINSTANCE

ctypedef LONG *PLONG
ctypedef LONG *LPLONG
ctypedef DWORD *PDWORD
ctypedef DWORD *LPDWORD
ctypedef WORD *PWORD
ctypedef WORD *LPWORD
ctypedef INT *PINT
ctypedef INT *LPINT

ctypedef LONGLONG *PLONGLONG
ctypedef ULONGLONG *PULONGLONG


ctypedef WCHAR TBYTE_UNICODE
ctypedef WCHAR TCHAR_UNICODE
ctypedef WCHAR *PTBYTE_UNICODE
ctypedef WCHAR *PTCHAR_UNICODE

ctypedef LPWSTR PTSTR_UNICODE
ctypedef LPWSTR LPTSTR_UNICODE

ctypedef LPCWSTR PCTSTR_UNICODE
ctypedef LPCWSTR LPCTSTR_UNICODE

ctypedef uint8_t TBYTE
ctypedef CHAR TCHAR
ctypedef TBYTE *PTBYTE
ctypedef TCHAR *PTCHAR

ctypedef LPSTR PTSTR
ctypedef LPSTR LPTSTR

ctypedef LPCSTR PCTSTR
ctypedef LPCSTR LPCTSTR

# UNICODE_STRING structure
ctypedef uint16_t USHORT

cdef struct UNICODE_STRING:
    USHORT Length
    USHORT MaximumLength
    PWSTR Buffer

ctypedef UNICODE_STRING *PUNICODE_STRING
ctypedef const UNICODE_STRING *PCUNICODE_STRING

# HRESULT
ctypedef LONG HRESULT

# HFILE
ctypedef INT HFILE

# LRESULT
ctypedef LONG_PTR LRESULT

# SC_LOCK
ctypedef LPVOID SC_LOCK

# USN
ctypedef LONGLONG USN

# Define RGB function
cdef inline DWORD RGB(BYTE red, BYTE green, BYTE blue):
    return red | (green << 8) | (blue << 16)

"""


def change_dtype_names(strsub):
    strsub = regex.sub(r"\bmap\b", "cpp_map", strsub)

    strsub = regex.sub(r"\bcomplex\b", "cpp_complex", strsub)
    strsub = regex.sub(r"\bqueue\b", "cpp_queue", strsub)
    strsub = regex.sub(r"\blist\b", "cpp_list", strsub)
    strsub = regex.sub(r"\bany\b", "cpp_any", strsub)
    strsub = regex.sub(r"\bdeque\b", "cpp_deque", strsub)
    strsub = regex.sub(r"\bset\b", "cpp_set", strsub)
    return strsub


def get_tmpfile(suffix=".txt"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = os.path.normpath(filename)
    tfp.close()
    return filename


def parse_cpp_data(parsedfile, headerfile, add_windows_dtypes=False):
    with open(parsedfile, "rb") as f:
        data = f.read()

    start = 0
    headerpath = rf"lambda at {headerfile}"
    for i in regex.finditer(rf"<{regex.escape(headerfile)}".encode(), data):
        start = i.start()
        break

    data = data[start:]
    dataforframe = []
    for i in regex.finditer(
        rb".*(?:(?:Function.*Decl)|(?:CXX.*Decl)|(?:TypeAlias.*Decl)).*", data
    ):
        if b"CXXConversionDecl" not in i.group(0):
            dataforframe.append(i.group(0))

    df2 = pd.DataFrame(dataforframe)
    df = (
        df2[0]
        .apply(
            lambda x: g[0].decode("utf-8", "ignore")
            if (g := regex.findall(rb"[^']+\s+'[^']+'", x))
            else pd.NA
        )
        .to_frame()
        .rename(columns={0: "aa_pystring"})
    )
    nanarrays = df.loc[df.aa_pystring.isna()].index.__array__()
    arraysplit = np.array_split(df, nanarrays)
    goodarrays = []
    objectcounter = 0
    for a in arraysplit:
        a2 = a.dropna(subset=["aa_pystring"], axis=0)
        if a2.empty:
            continue
        try:
            if a2.loc[a2.aa_pystring.str.contains(headerpath, regex=False)].empty:
                goodarrays.append(a2.assign(aa_object=objectcounter))
                objectcounter += 1
        except Exception as e:
            print(e)

    df = pd.concat(goodarrays, ignore_index=True)
    df.aa_pystring = df.aa_pystring.str.split(
        r"(?:line|col):[\d:]+\s+", regex=True
    ).str[-1]
    df["aa_returntype"] = (
        df.aa_pystring.str.replace(r"^[^']+'", "", regex=True)
        .str.split("(", regex=False)
        .str[0]
        .str.strip()
        .str.replace("<", "[", regex=False)
        .str.replace(">", "]", regex=False)
        .str.replace(r"\b[\w:]+::", "", regex=True)
        .str.replace(r"\s+::", " ", regex=True)
    )
    df["aa_argtypes"] = (
        df.aa_pystring.str.replace(r"^[^\(]+\(", "", regex=True)
        .str.split(")", regex=False)
        .str[0]
        .str.strip()
        .str.replace("<", "[", regex=False)
        .str.replace(">", "]", regex=False)
        .str.replace(r"\b[\w:]+::", "", regex=True)
        .str.replace(r"\s+::", " ", regex=True)
    )

    df["aa_methodname"] = (
        df.aa_pystring.str.split("'", regex=False).str[0].str.split().str[-1]
    )
    opindex = df.loc[df.aa_pystring.str.contains("operator")].index
    df.loc[opindex, "aa_methodname"] = (
        df.loc[opindex, "aa_pystring"]
        .str.replace("^.*operator", "operator", regex=True)
        .str.split(" '")
        .str[0]
        .str.strip()
    )

    typedefs = df.loc[
        (~df.aa_pystring.str.contains("(", regex=False, na=False))
        & (~df.aa_pystring.str.contains(")", regex=False, na=False))
        & (df.aa_pystring.str.contains("'", regex=False, na=False))
    ].index

    df.loc[typedefs, "aa_returntype"] = df.loc[typedefs, "aa_returntype"].apply(
        lambda q: f"""ctypedef {str(q).replace("'", "")}"""
    )

    destructors = (
        df.loc[
            df.aa_pystring.str.contains(
                r"~\w+\s+'void.*noexcept'", regex=True, na=False
            )
        ]
        .aa_pystring.str.extract(r"~(\w+)\s+'void.*noexcept'")
        .drop_duplicates(subset=0)
        .copy()
    )

    dfx = df.copy(deep=True)
    for key, item in destructors.iterrows():
        first_ele = df.loc[df.aa_pystring.str.contains(item[0])]
        first_index = first_ele.index[0]
        insert_index = first_index - 0.5
        dfx.loc[insert_index, "aa_methodname"] = f"cdef cppclass {item[0]}:"
        dfx.loc[insert_index, "aa_object"] = first_ele.iloc[0]["aa_object"]
    df = dfx.sort_index().reset_index(drop=True).fillna("")
    df.loc[typedefs, "aa_argtypes"] = ""
    purefilehname = os.path.basename(headerfile)
    firstlinetoadd = f'cdef extern from "{purefilehname}" nogil :'
    importstringlist = [firstlinetoadd]
    classindent = "    "
    for name, group in df.groupby("aa_object"):
        importstringlist.append("")
        for key, item in group.iterrows():
            if (
                "ctypedef " not in f"{item.aa_returntype}"
                and "cdef cppclass " not in f"{item.aa_methodname}"
            ):
                addargs = ""
                if regex.search(r"\b[A-Z]\b", f"{item.aa_argtypes}"):
                    item_aa_argtypes = regex.sub(
                        r"(\b[A-Z]\b)", r"[\g<1>]", f"{item.aa_argtypes}"
                    )
                    templateargs = []
                    splittypes = regex.split(r"\[+", item_aa_argtypes)
                    for sty in splittypes:
                        if "]" in sty:
                            tmpspli = regex.split(r"\]+", sty)[0]
                            templateargs.extend(regex.split(r"\W+", tmpspli))
                    if splittypes:
                        addargs = "[" + ", ".join(templateargs) + "]"

                new_item_aa_returntype = change_dtype_names(f"{item.aa_returntype}")
                new_item_aa_argtypes = change_dtype_names(f"{item.aa_argtypes}")
                importstringlist.append(
                    f"{classindent}{new_item_aa_returntype} {item.aa_methodname}{addargs}({new_item_aa_argtypes})"
                )
            elif "cdef cppclass " in f"{item.aa_methodname}":
                importstringlist.append(f"    {item.aa_methodname}")
                classindent = "        "
            else:
                new_item_aa_returntype = change_dtype_names(f"{item.aa_returntype}")

                importstringlist.append(
                    f"{classindent}{new_item_aa_returntype} {item.aa_methodname}"
                )
            if len(importstringlist) > 1 and "void ~" in importstringlist[-1]:
                del importstringlist[-1]
                classindent = "    "

    if not add_windows_dtypes:
        return (
            (importstoadd + "\n" + "\n".join(importstringlist))
            .strip()
            .replace(" ::", " ")
        )
    else:
        return (
            (importstoadd + "\n" + windtypes + "\n" + "\n".join(importstringlist))
            .strip()
            .replace(" ::", " ")
        )


def create_pxd_file(
    hfile,
    pxdout,
    clangpp_exe=r"C:\Program Files\LLVM\bin\clang++.exe",
    additonal_args=("-std=c++20",),
    add_windows_dtypes=False,
):
    mytmpfile = get_tmpfile(suffix=".txt")

    must_have_args = [
        f'"{clangpp_exe}"',
        *additonal_args,
        "-Xclang",
        "-ast-dump",
        f'"{hfile}"',
        ">",
        mytmpfile,
    ]

    wholecommand = " ".join(must_have_args) + '\necho "done"\nexit\n'
    subprocess.run(os.environ.get("COMSPEC"), shell=True, input=wholecommand.encode())
    importstringlist = parse_cpp_data(
        parsedfile=mytmpfile, headerfile=hfile, add_windows_dtypes=add_windows_dtypes
    )
    try:
        os.remove(mytmpfile)
    except Exception as e:
        print(e)
    touch(pxdout)
    with open(pxdout, "w", encoding="utf-8") as f:
        f.write(importstringlist)
    return importstringlist
