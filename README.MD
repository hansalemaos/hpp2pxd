# Converts C++ header files into Cython PXD files

If you don't succeed converting your C++ header file to PXD files using [autopxd2](https://github.com/elijahr/python-autopxd2), you can try this little function. 
The results aren't as good as autopxd2, but it always outputs something. Most of the time, you will need to readjust some things, but it will save you a lot of time.
Autopxd2, unfortunately, crashes quite often, this is why I wrote this script. 

## Install LLVM, I use the [choco version](https://community.chocolatey.org/packages/llvm) 

## Run the script

```py
# Example from https://github.com/hansalemaos/PythonString_for_CPP/blob/main/pythonstring.h
from hpp2pxd import create_pxd_file

create_pxd_file(
    hfile=r"C:\basjx\PythonString_for_CPP\pythonstring.h",
    pxdout=r"C:\basjx\PythonString_for_CPP\pythonstring.pxd",
    clangpp_exe=r"C:\Program Files\LLVM\bin\clang++.exe",
    additonal_args=("-std=c++20",),
)
```

## Output

### Not 100% perfect, but certainly a good base

```py
# By default, it imports everything it can from C++
# Just delete what you don't need 
from libc.stdint cimport *
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
from libc.stddef import * 
cdef extern from "pythonstring.h" nogil :

    void reverse_strings(vector[string] &)
    void split_whitespace(const string_view, vector[string] &, int)
    void rsplit_whitespace(const string_view, vector[string] &, int)
    vector[size_t] find_all_indices_strviewfind(const string_view, const string_view)
    void split_at_string(const string_view, const string_view, vector[string] &)
    void split(const string_view, vector[string] &, const string_view, int)
    void rsplit(const string_view, vector[string] &, const string_view, int)
    string do_strip(const string_view, int, const string_view)
    string strip(const string_view, const string_view)
    string lstrip(const string_view, const string_view)
    string rstrip(const string_view, const string_view)
    string join(const string, const vector[string] &)
    int _string_tailmatch(const string_view, const string_view, Py_ssize_t, Py_ssize_t, int)
    bool endswith(const string_view, const string_view, int, int)
    bool _endswith(const string_view, const string_view, int, int)
    bool startswith(const string_view, const string_view, int, int)
    bool _startswith(const string_view, const string_view, int, int)
    bool is_bool(const string_view)
    bool is_int_number(const string_view)
    bool is_float_number(const string_view)
    bool isalnum(const string_view)
    bool isalpha(const string_view)
    bool isdigit(const string_view)
    bool islower(const string_view)
    bool isspace(const string_view)
    bool istitle(const string_view)
    bool isupper(const string_view)
    string capitalize(const string_view)
    string lower(const string_view)
    string upper(const string_view)
    string swapcase(const string_view)
    string title(const string_view)
    string translate(const string_view, const string_view, const string_view)
    string zfill(const string_view, int)
    string ljust(const string_view, int, char)
    string rjust(const string_view, int, char)
    string center(const string_view, int, char)
    string slice(const string_view, int, int)
    int find(const string_view, const string_view, int, int)
    int index(const string_view, const string_view, int, int)
    int rfind(const string_view, const string_view, int, int)
    int rindex(const string_view, const string_view, int, int)
    void partition(const string_view, const string_view, vector[string] &)
    void rpartition(const string_view, const string_view, vector[string] &)
    string expandtabs(const string_view, int)
    int count(const string_view, const string_view, int, int)
    string replace(const string_view, const string_view, const string_view, int)
    void splitlines(const string_view, vector[string] &, bool)
    string __mul__(const string_view, int)
    void generate_random_alphanumstring(char *, size_t)
    string removeprefix(const string_view, const string_view)
    string removesuffix(const string_view, const string_view)
    variant[double, int64_t] to_float_or_int(string_view)
    bool check_if_string_is_valid_float_zero(const string_view)
    bool check_if_string_is_valid_int_zero(const string_view)
    bool is_binary_notation(const string_view)
    bool is_hex_notation_upper_with_0x(const string_view)
    bool is_hex_notation_upper_without_0x(const string_view)
    bool is_hex_notation_lower_with_0x(const string_view)
    bool is_hex_notation_lower_without_0x(const string_view)
    bool is_octal_notation(const string_view)
    bool is_any_valid_number(const string_view)
    string normalize_whitespaces(const string_view &)
    string remove_whitespaces(const string_view)
    string to_padded(int, char, const string_view)
    string replace_fu(const string_view, int)
    int calc_best_substring_distance(const string_view, const string_view, int)
    void boyer_moore_horspool_searcher_all(const string_view, const string_view, vector[size_t] &)
    string convert_mem_address_to_string(size_t, size_t)
    string string_from_sv_vector(const vector[string_view] &)
    string string_from_s_vector(const vector[string] &)
    string string_from_constchar_array(const char **, size_t)
    string string_from_char_vector(const vector[char] &)
    string string_from_char_ptr_vector(const vector[char *] &)
    ctypedef pair[int, int] PY_RANGE
    ctypedef vector[int] PY_INT_VEC
    ctypedef size_t PY_SIZE_T
    ctypedef pair[PY_INT_VEC, string] PY_CHR_PTR_LIST
    ctypedef vector[char] PY_CHAR_VEC
    ctypedef unordered_map[unsigned char, unsigned char] PY_TRANSLATION_TABLE
    ctypedef vector[string] PY_STRING_VEC
    ctypedef unordered_map[string, string] PY_STRING_DICT_UNORDERED
    ctypedef cpp_map[string, string] PY_STRING_DICT

    void length_sorter(vector[int] &, vector[string_view] &)

    cdef cppclass SliceObject:
        void SliceObject(vector[char *])
        SliceObject & operator=(string)
        SliceObject & operator=(const string_view)
        SliceObject & operator=(char)
        SliceObject & operator=(const char *)
        SliceObject & operator=(vector[char])
        void SliceObject(const SliceObject &)
        void SliceObject(SliceObject &&)
        SliceObject & operator=(const SliceObject &)
        SliceObject & operator=(SliceObject &&)

    cdef cppclass PythonString:
        void PythonString(SliceObject &&)

        void PythonString(auto)
        void PythonString(basic_string[char])
        void PythonString(vector[basic_string_view[char]])
        void PythonString(basic_string_view[char])
        void PythonString(PythonString)
        void PythonString(vector[char])
        void PythonString(const vector[char *] &)
        void PythonString(const vector[unique_ptr[char]] &)
        void PythonString(const char *)
        void PythonString(const string &)
        void PythonString(string &&)
        void PythonString(const string_view)
        void PythonString(PY_SIZE_T, PY_SIZE_T)
        void PythonString(void *)
        void PythonString(const PY_STRING_VEC &)
        void PythonString(const PY_CHAR_VEC &)
        void PythonString(vector[string_view])
        void PythonString(const char **, PY_SIZE_T)
        void PythonString(const PythonString &)
        void PythonString(PythonString &&)
        PythonString & operator=(const string_view)
        PythonString & operator=(const char *)
        PythonString & operator=(const string &)
        PythonString & operator=(const PythonString &)

        PythonString join[T](vector[T])
        PythonString join(vector[PythonString])
        PythonString to_format_Black()
        PythonString to_format_Red()
        PythonString to_format_Green()
        PythonString to_format_Yellow()
        PythonString to_format_Blue()
        PythonString to_format_Purple()
        PythonString to_format_Cyan()
        PythonString to_format_White()
        PythonString to_format_BBlack()
        PythonString to_format_BRed()
        PythonString to_format_BGreen()
        PythonString to_format_BYellow()
        PythonString to_format_BBlue()
        PythonString to_format_BPurple()
        PythonString to_format_BCyan()
        PythonString to_format_BWhite()
        PythonString to_format_UBlack()
        PythonString to_format_URed()
        PythonString to_format_UGreen()
        PythonString to_format_UYellow()
        PythonString to_format_UBlue()
        PythonString to_format_UPurple()
        PythonString to_format_UCyan()
        PythonString to_format_UWhite()
        PythonString to_format_On_Black()
        PythonString to_format_On_Red()
        PythonString to_format_On_Green()
        PythonString to_format_On_Yellow()
        PythonString to_format_On_Blue()
        PythonString to_format_On_Purple()
        PythonString to_format_On_Cyan()
        PythonString to_format_On_White()
        PythonString to_format_IBlack()
        PythonString to_format_IRed()
        PythonString to_format_IGreen()
        PythonString to_format_IYellow()
        PythonString to_format_IBlue()
        PythonString to_format_IPurple()
        PythonString to_format_ICyan()
        PythonString to_format_IWhite()
        PythonString to_format_BIBlack()
        PythonString to_format_BIRed()
        PythonString to_format_BIGreen()
        PythonString to_format_BIYellow()
        PythonString to_format_BIBlue()
        PythonString to_format_BIPurple()
        PythonString to_format_BICyan()
        PythonString to_format_BIWhite()
        PythonString to_format_On_IBlack()
        PythonString to_format_On_IRed()
        PythonString to_format_On_IGreen()
        PythonString to_format_On_IYellow()
        PythonString to_format_On_IBlue()
        PythonString to_format_On_IPurple()
        PythonString to_format_On_ICyan()
        PythonString to_format_On_IWhite()
        PythonString operator+(const PythonString &)
        PythonString operator+(const string_view)
        PythonString operator+(const string &)
        PythonString operator+(const char *)

        PythonString operator+(auto)
        PythonString operator+(PythonString)
        PythonString operator+(const char *)
        uint32_t calculate_hash()
        void _check_if_start_end_valid(int, int)
        int _get_real_index_or_raise(int)
        PythonString operator*(size_t)
        char & operator[](int)
        PythonString operator[](PY_RANGE)
        SliceObject operator[](PY_SLICE &&)
        vector[char] operator[](const PY_INT_VEC)
        PythonString & reverse_inplace()
        PythonString reverse()
        PythonString print_green(const string &)
        PythonString print_red(const string &)
        PythonString print_yellow(const string &)
        PythonString print_cyan(const string &)
        PythonString print_magenta(const string &)
        PythonString print_bg_green(const string &)
        PythonString print_bg_red(const string &)
        PythonString print_bg_yellow(const string &)
        PythonString print_bg_cyan(const string &)
        PythonString print_bg_magenta(const string &)
        void print_to_std_err()
        vector[PythonString] _return_pystring_vec(vector[string] &&)
        vector[PythonString] split(const PythonString &, int)
        vector[PythonString] split(const string &, int)
        vector[PythonString] split(string &&, int)
        vector[PythonString] split(string &&)
        vector[PythonString] split(const char *, int)
        vector[PythonString] split(const string_view, int)
        vector[PythonString] split(int)

        vector[PythonString] split[T](const T &)
        vector[PythonString] split(const int &)
        vector[PythonString] split()
        vector[PythonString] operator/(PythonString &&)
        vector[PythonString] operator/(const PythonString &)
        vector[PythonString] operator/(const string_view)
        vector[PythonString] operator/(string &&)
        vector[PythonString] operator/(const string &)
        vector[PythonString] operator/(const char *)
        vector[PythonString] operator/(int)
        bool operator==(const PythonString &)
        bool operator!=(const PythonString &)
        bool operator<(const PythonString &)
        bool operator>(const PythonString &)
        bool operator>=(const PythonString &)
        bool operator<=(const PythonString &)
        vector[uint8_t] convert_to_uint8(int)
        bool endswith(const string_view, int, int)
        bool endswith(const string &, int, int)
        bool endswith(const char *, int, int)
        bool endswith(const PythonString &, int, int)

        bool endswith[T](const T &)
        bool startswith(const string_view, int, int)
        bool startswith(const string &, int, int)
        bool startswith(const char *, int, int)
        bool startswith(const PythonString &, int, int)

        bool startswith[T](const T &)
        bool isspace()
        bool isalnum()
        bool isalpha()
        bool isdigit()
        bool islower()
        bool istitle()
        bool isupper()
        bool isint()
        bool isdecimal()
        bool isfloat()
        bool isbool()
        variant[double, int64_t] convert_to_number()
        bool convert_to_bool()
        bool is_ascii()
        bool isprintable()
        int64_t convert_to_int_at_any_cost(int64_t)
        double convert_to_double_at_any_cost(double)
        vector[PythonString] operator%(int)
        vector[PythonString] operator%=(int)
        vector[PythonString] splitlines(bool)
        vector[PythonString] splitlines()
        vector[PythonString] rsplit(const PythonString &, int)
        vector[PythonString] rsplit(const string &, int)
        vector[PythonString] rsplit(const char *, int)
        vector[PythonString] rsplit(const string_view, int)
        vector[PythonString] rsplit(int)
        vector[PythonString] rsplit()

        vector[PythonString] rsplit[T](const T &)
        PythonString strip(const string_view)
        PythonString strip(const string &)
        PythonString strip(const char *)
        PythonString strip(const PythonString &)
        PythonString strip(PY_CHAR_VEC &)
        PythonString strip()

        PythonString & strip_inplace[T](const T &)
        PythonString & strip_inplace()
        PythonString rstrip(const string_view)
        PythonString rstrip(const string &)
        PythonString rstrip(const char *)
        PythonString rstrip(const PythonString &)
        PythonString rstrip(PY_CHAR_VEC &)
        PythonString rstrip()

        PythonString & rstrip_inplace[T](const T &)
        PythonString & rstrip_inplace()
        PythonString lstrip(const string_view)
        PythonString lstrip(const string &)
        PythonString lstrip(const char *)
        PythonString lstrip(const PythonString &)
        PythonString lstrip(PY_CHAR_VEC &)
        PythonString lstrip()

        PythonString & lstrip_inplace[T](const T &)
        PythonString & lstrip_inplace()
        size_t size()
        string to_cpp_string_copy()
        string & to_cpp_string()
        const char * c_str()
        char * c_str_muteable()
        iterator begin()
        iterator end()
        const_iterator cbegin()
        const_iterator cend()
        reverse_iterator rbegin()
        reverse_iterator rend()
        const_reverse_iterator crbegin()
        const_reverse_iterator crend()
        string _create_translation_table(const unordered_map[unsigned char, unsigned char] &)
        PythonString translate(PY_TRANSLATION_TABLE, const string &)
        PythonString translate(PY_TRANSLATION_TABLE, const string_view)
        PythonString translate(PY_TRANSLATION_TABLE, const char *)
        PythonString translate(PY_TRANSLATION_TABLE)

        PythonString & translate_inplace[T](PY_TRANSLATION_TABLE, const T &)
        PythonString & translate_inplace(PY_TRANSLATION_TABLE)
        PythonString zfill(int32_t)
        PythonString & zfill_inplace(int32_t)
        PythonString rjust(int32_t, char)
        PythonString rjust(int32_t, const string &)
        PythonString rjust(int32_t)

        PythonString & rjust_inplace[T](int32_t, T)
        PythonString & rjust_inplace(int32_t)
        PythonString ljust(int32_t)
        PythonString ljust(int32_t, char)
        PythonString ljust(int32_t, const string &)

        PythonString & ljust_inplace[T](int32_t, T)
        PythonString & ljust_inplace(int32_t)
        PythonString center(int32_t, char)
        PythonString center(int32_t, const string &)
        PythonString center(int32_t)

        PythonString & center_inplace[T](int32_t, T)
        PythonString & center_inplace(int32_t)
        int find(const PythonString &, int, int)
        int find(const string_view, int, int)
        int find(const char *, int, int)
        int find(const string &, int, int)

        int find[T](const T)

        int index[T](const T, int, int)

        int index[T](const T)
        int rfind(const PythonString &, int, int)
        int rfind(const string_view, int, int)
        int rfind(const char *, int, int)
        int rfind(const string &, int, int)

        int rfind[T](const T)

        int rindex[T](const T, int, int)

        int rindex[T](const T)
        PythonString expandtabs(int32_t)
        PythonString expandtabs()
        PythonString & expandtabs_inplace(int32_t)
        PythonString & expandtabs_inplace()
        int count(const string_view, int, int)
        int count(const char *, int, int)
        int count(char, int, int)
        int count(const string &, int, int)
        int count(const PythonString &, int, int)
        cpp_map[string, int] count(const vector[string] &, int, int)

        int count[T](const T)
        cpp_map[string, int] count(const vector[string] &)
        PythonString replace(const PythonString &, const PythonString &, int)
        PythonString replace(const string_view, const string_view, int)
        PythonString replace(const char *, const char *, int)
        PythonString replace(const string &, const string &, int)

        PythonString replace[T, U](const T, const U)
        PythonString replace(const char *const, const char *const)
        PythonString replace(const basic_string[char], const basic_string[char])

        PythonString replace_inplace[T, U](const T, const U, int)

        PythonString replace_inplace[T, U](const T, const U)
        PythonString removeprefix(const PythonString &)
        PythonString removeprefix(const string_view)
        PythonString removeprefix(const char *)
        PythonString removeprefix(const string &)

        PythonString & removeprefix_inplace[T](const T)
        PythonString removesuffix(const PythonString &)
        PythonString removesuffix(const string_view)
        PythonString removesuffix(const char *)
        PythonString removesuffix(const string &)

        PythonString & removesuffix_inplace[T](const T)
        vector[PythonString] partition(const PythonString &)
        vector[PythonString] partition(PythonString &&)
        vector[PythonString] partition(const char *)
        vector[PythonString] partition(string &&)
        vector[PythonString] partition(const string &)
        vector[PythonString] partition(const string_view)
        vector[PythonString] partition(char)
        vector[PythonString] rpartition(const PythonString &)
        vector[PythonString] rpartition(PythonString &&)
        vector[PythonString] rpartition(const char *)
        vector[PythonString] rpartition(string &&)
        vector[PythonString] rpartition(const string &)
        vector[PythonString] rpartition(const string_view)
        vector[PythonString] rpartition(char)
        PythonString capitalize_each_word()
        PythonString & capitalize_each_word_inplace()
        PythonString capitalize()
        PythonString & capitalize_inplace()
        PythonString lower()
        PythonString & lower_inplace()
        PythonString upper()
        PythonString & upper_inplace()
        PythonString swapcase()
        PythonString & swapcase_inplace()
        PythonString title()
        PythonString & title_inplace()
        size_t calculate_string_hash_static(const string_view)
        PythonString insert_strings_at_indices(vector[pair[int, string]] &)
        PythonString insert_strings_at_indices(vector[pair[int, PythonString]] &)

        PythonString & insert_strings_at_indices_inplace[T](T &)
        vector[PythonString] split_at_multi_string(const vector[PythonString] &)
        cpp_map[size_t, PythonString] split_at_multi_string_keep_strings(vector[string] &)
        cpp_map[size_t, PythonString] split_at_multi_string_keep_strings(vector[string] &&)
        cpp_map[size_t, PythonString] split_at_multi_string_keep_strings(vector[PythonString] &)
        size_t len()
        vector[PythonString] split_strtok(const string &)
        PythonString casefold()
        PythonString & casefold_inplace()
        PythonString remove_accents()
        PythonString & remove_accents_inplace()
        bool is_bin_oct_hex_dec()
        bool is_oct_number()
        bool is_hex_number_with_0x()
        bool is_hex_number_without_0x()
        bool is_binary_with_0b()
        PythonString generate_random_alphanumeric_string(size_t)
        vector[PythonString] read_file_to_string_vector(const char *)
        vector[PythonString] read_file_to_string_vector(const string &)
        vector[PythonString] read_file_to_string_vector(const string_view)
        vector[PythonString] read_file_to_string_vector(const PythonString &)
        PythonString from_file(const char *)
        PythonString from_file(const string &)
        PythonString from_file(string &&)
        PythonString from_file(const string_view)
        PythonString from_file(const PythonString &)
        PythonString from_file(PythonString &&)
        vector[PythonString] split_at_multi_string(PY_STRING_VEC &)
        vector[PythonString] split_at_multi_string(PY_STRING_VEC &&)
        void save_as_file(const char *)
        void append_to_file(const char *)
        bool in(const string_view)
        bool in(const PythonString &)
        bool in(const string &)
        bool in(const char *)
        vector[size_t] find_me_everywhere_in_another_string(const PythonString &)
        vector[size_t] find_me_everywhere_in_another_string(const string_view)
        vector[size_t] find_me_everywhere_in_another_string(const char *)
        vector[size_t] find_me_everywhere_in_another_string(const string &)

        PythonString format(Args...)

        PythonString & format_inplace(Args...)

        PythonString format_map[T](const T &)

        PythonString & format_map_inplace[T](const T &)
        vector[size_t] find_subststring_everywhere_in_me(const PythonString &)
        vector[size_t] find_subststring_everywhere_in_me(const string_view)
        vector[size_t] find_subststring_everywhere_in_me(const char *)
        vector[size_t] find_subststring_everywhere_in_me(const string &)
        unordered_map[string, vector[size_t]] find_subststrings_everywhere_in_me(const vector[string] &)
        PythonString convert_to_base16()
        PythonString & convert_to_base16_inplace()
        PythonString from_base16(const string &)
        PythonString & from_base16_inplace()
        vector[PythonString] split_and_beginning_of_multiple_strings(const vector[string] &, const string_view, const string_view)
        PythonString & split_and_beginning_of_multiple_strings_inplace(const vector[string] &, const string_view, const string_view, const string_view)
        PythonString normalize_whitespaces()
        PythonString & normalize_whitespaces_inplace()
        PythonString remove_whitespaces()
        PythonString & remove_whitespaces_inplace()
        PythonString pad_string(int)
        PythonString & pad_string_inplace(int)
        PythonString pad_string(int, char)
        PythonString & pad_string_inplace(int, char)
        PythonString replace_non_alphanumeric_with_spaces()
        PythonString replace_non_printable_with_spaces()
        PythonString replace_non_decimal_with_spaces()
        PythonString & replace_non_alphanumeric_with_spaces_inplace()
        PythonString & replace_non_printable_with_spaces_inplace()
        PythonString & replace_non_decimal_with_spaces_inplace()
        int hamming_distance_best_fit(const PythonString &)
        int hamming_distance_best_fit(const string_view)
        int hamming_distance_best_fit(const string &)
        int hamming_distance_best_fit(const char *)
        int substring_distance_best_fit_v1(const PythonString &)
        int substring_distance_best_fit_v1(const string_view)
        int substring_distance_best_fit_v1(const string &)
        int substring_distance_best_fit_v1(const char *)
        int substring_distance_best_fit_v2(const PythonString &)
        int substring_distance_best_fit_v2(const string_view)
        int substring_distance_best_fit_v2(const string &)
        int substring_distance_best_fit_v2(const char *)
        int substring_distance_best_fit_v3(const PythonString &)
        int substring_distance_best_fit_v3(const string_view)
        int substring_distance_best_fit_v3(const string &)
        int substring_distance_best_fit_v3(const char *)
        vector[size_t] boyer_moore_horspool_searcher_all(const string_view)
        vector[size_t] boyer_moore_horspool_searcher_all(const PythonString &)
        vector[size_t] boyer_moore_horspool_searcher_all(const string &)
        vector[size_t] boyer_moore_horspool_searcher_all(const char *)
        unordered_map[string, int] count_word_frequency()
        vector[string] get_unique_words()
        PythonString remove_duplicated_substrings_keep_first()
        vector[int] argsort_by_(vector[string_view] &, int)
        vector[int] argsort_by_(const vector[string] &, int)
        vector[int] argsort_by_(const vector[PythonString] &, int)
        vector[PythonString] sort_by_(vector[string_view] &, int)
        vector[PythonString] sort_by_(const vector[string] &, int)
        vector[PythonString] sort_by_(const vector[PythonString] &, int)

        vector[PythonString] sort_by_length[T](const T &)

        vector[int] argsort_by_length[T](const T &)

        vector[PythonString] sort_by_alphabet[T](const T &)

        vector[int] argsort_by_alphabet[T](const T &)

        vector[PythonString] sort_by_alphabet_reverse[T](const T &)

        vector[int] argsort_by_alphabet_reverse[T](const T &)

        vector[PythonString] sort_by_alphabet_ignore_case[T](const T &)

        vector[int] argsort_by_alphabet_ignore_case[T](const T &)

        vector[PythonString] sort_by_alphabet_reverse_ignore_case[T](const T &)

        vector[int] argsort_by_alphabet_reverse_ignore_case[T](const T &)

        vector[PythonString] sort_by_alphabet_avarage_ignore_case[T](const T &)

        vector[int] argsort_by_alphabet_avarage_ignore_case[T](const T &)
    ostream & operator<<(ostream &, const PythonString &)
    ostream & operator<<(ostream &, const vector[PythonString] &)

    ostream & operator<<[T](ostream &, const vector[vector[T]] &)

    ostream & operator<<[T](ostream &, const vector[T] &)

    ostream & operator<<[T](ostream &, const cpp_set[T] &)

    ostream & operator<<[T](ostream &, const unordered_set[T] &)

    ostream & operator<<[T](ostream &, const cpp_list[T] &)

    ostream & operator<<[T, N](ostream &, const array[T, N] &)

    ostream & operator<<[T, U](ostream &, const cpp_map[T, U] &)

    ostream & operator<<[T, U](ostream &, const unordered_map[T, U] &)
    ostream & operator<<(ostream &, const SliceObject &)
    void enable_srand()

    size_t operator()()
```

