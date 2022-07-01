# Import Packages and Modules
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
import  unittest
from    TextLoader  import *


# Write Function For UnitTest
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
def writeFileFromList(fileName:str, tList:list, encodingFormat:str):
    with open(fileName, 'w', encoding=encodingFormat) as wf:
        if tList:
            for line in tList:
                wf.write(f'{line}\n')


# Defines
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
TEST_TXT_LIST           = ['123', 'abc', 'A1B2C3', '!@#$%^&', 'ㄱㄴㄷ', '가나다라마바사']
EMPTY_TXT_LIST          = []

UTF8                    = 'UTF-8'
ASCII                   = 'ASCII'

UNITTEST_DIR            = './UnitTest'
FILE_UTF8_NAME          = f'{UNITTEST_DIR}/UnitTest_UTF8.txt'
FILE_ASCII_NAME         = f'{UNITTEST_DIR}/UnitTest_ASCII.txt'
FILE_EMPTY_UTF8_NAME    = f'{UNITTEST_DIR}/UnitTest_Empty_UTF8.txt'
FILE_EMPTY_ASCII_NAME   = f'{UNITTEST_DIR}/UnitTest_Empty_ASCII.txt'
WRONG_FILE_NAME         = f'{UNITTEST_DIR}/noneExistFile.txt'


# TestCase
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
class CustomTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """ Before Start UnitTest"""
        if os.path.isdir(UNITTEST_DIR) is False:
            os.makedirs(UNITTEST_DIR, exist_ok=True)

        writeFileFromList(FILE_UTF8_NAME,           TEST_TXT_LIST,  'utf-8')
        writeFileFromList(FILE_ASCII_NAME,          TEST_TXT_LIST,  'mbcs' )
        writeFileFromList(FILE_EMPTY_UTF8_NAME,     EMPTY_TXT_LIST, 'utf-8')
        writeFileFromList(FILE_EMPTY_ASCII_NAME,    EMPTY_TXT_LIST, 'mbcs' )

    @classmethod
    def tearDownClass(cls) -> None:
        """ After Finish Unit Test """
        if os.path.isfile(FILE_UTF8_NAME):
            os.remove(FILE_UTF8_NAME)

        if os.path.isfile(FILE_ASCII_NAME):
            os.remove(FILE_ASCII_NAME)

        if os.path.isfile(FILE_EMPTY_UTF8_NAME):
            os.remove(FILE_EMPTY_UTF8_NAME)

        if os.path.isfile(FILE_EMPTY_ASCII_NAME):
            os.remove(FILE_EMPTY_ASCII_NAME)

        if os.path.isdir(UNITTEST_DIR):
            os.rmdir(UNITTEST_DIR)


    # TEST
    # *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
    """
        I. 파일 등록 방법
            1. TextLoader 클래스 생성 시 인자로 즉시 넘김
            2. setFile 사용
            3. 각 함수에 직접 입력
        
        II. 파일 유형
            1. 유효한 파일 : UTF-8
            2. 유효한 파일 : ASCII
            3. 빈 파일 : UTF-8
            4. 빈 파일 : ASCII
            5. 존재하지 않는 파일

        III. get 함수
            1. fileName
            2. encoding ( private, public method, overloading func )
            3. textList ( public method, overloading func )
    """

    # File Register + get FileName Test
    # *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
    #01 
    # I.1 + II.1 + III.1) TextLoader 생성자 옳은 파일 이름 입력
    def test_set_right_filename_when_class_create(self):
        tL = TextLoader(FILE_UTF8_NAME)
        self.assertIsNotNone(tL.getFileName())

    #02
    # I.1 + III.1) TextLoader 생성자 파일 이름 입력 안함
    def test_not_set_filename_when_class_create(self):
        tL = TextLoader()
        self.assertIsNone(tL.getFileName())

    #03
    # I.1 + II.5) TextLoader 생성자 잘못된 파일 이름 입력
    def test_set_wrong_filename_when_class_create(self):
        self.assertRaises(Exception, TextLoader, WRONG_FILE_NAME)

    #04
    # I.1 + II.1 + III.1) TextLoader 생성 시 파일 이름 입력했을 때, getFileName() 
    def test_get_right_filename_when_class_create(self):
        tL = TextLoader(FILE_UTF8_NAME)
        self.assertEqual(tL.getFileName(), FILE_UTF8_NAME)

    # I.1 + III.1) TextLoader 생성 시 파일 이름 입력 안했을 때, getFileName()
    # Case02 와 동일

    #05
    # I.2 + II.1 + III.1) TextLoader 생성 이후에 옳은 파일 이름 setFile()
    def test_set_right_filename_when_setFile_after_class_create(self):
        tL = TextLoader()
        tL.setFile(FILE_UTF8_NAME)
        self.assertIsNotNone(tL.getFileName())

    #06
    # I.2 + II.5) TextLoader 생성 이후에 잘못된 파일 이름 setFile()
    def test_set_wrong_filename_when_setFile_after_class_create(self):
        tL = TextLoader()
        self.assertRaises(Exception, tL.setFile, WRONG_FILE_NAME)

    #07
    # I.2 + II.2 + III.1) TextLoader 생성 이후에 여러 번 setFile(), 모두 옳은 파일
    def test_setFile_multiple_all_right(self):
        tL = TextLoader()
        tL.setFile(FILE_UTF8_NAME)
        tL.setFile(FILE_EMPTY_UTF8_NAME)
        tL.setFile(FILE_ASCII_NAME)
        self.assertEqual(tL.getFileName(), FILE_ASCII_NAME)

    #08
    # I.2 + II.5) TextLoader 생성 이후에 여러 번 setFile(), 중간 잘못된 파일
    def test_setFile_multiple_one_wrong(self):
        tL = TextLoader()
        tL.setFile(FILE_UTF8_NAME)
        tL.setFile(FILE_EMPTY_UTF8_NAME)
        self.assertRaises(Exception, tL.setFile, WRONG_FILE_NAME)

    #09
    # I.2 + II.1 + III.1) TextLoader 생성자 옳은 파일 이름 입력 이후 다른 파일 setFile
    def test_set_right_filename_when_setFile_already_set_filename(self):
        tL = TextLoader(FILE_ASCII_NAME)
        tL.setFile(FILE_UTF8_NAME)
        self.assertEqual(tL.getFileName(), FILE_UTF8_NAME)


    # Get Encoding Test :: private Function : _getFileEncoding()
    # *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
    #10
    # I.1 + II.1 + III.2) TextLoader 생성자 옳은 파일 이름 입력 + private _getFileEncoding()
    def test_get_encoding_privFunc_when_class_create(self):
        tL = TextLoader(FILE_UTF8_NAME)
        self.assertEqual(tL._getFileEncoding(), UTF8)

    #11
    # I.1 + II.2 + III.2) TextLoader 생성자 옳은 파일 이름 입력 + private _getFileEncoding(other file)
    def test_get_newReg_encoding_privFunc_when_class_create(self):
        tL = TextLoader(FILE_UTF8_NAME)
        self.assertEqual(tL._getFileEncoding(FILE_ASCII_NAME), ASCII)

    #12
    # I.1 + III.2) TextLoader 생성자 파일 이름 입력 안함 + private _getFileEncoding()
    def test_get_encoding_privFunc_when_not_set_filename_ever(self):
        tL = TextLoader()
        self.assertRaises(Exception, tL._getFileEncoding)

    #13
    # I.1 + III.2) TextLoader 생성자 파일 이름 입력 안함 + private _getFileEncoding(file)
    def test_get_newReg_encoding_privFunc_when_not_set_class_create(self):
        tL = TextLoader()
        self.assertEqual(tL._getFileEncoding(FILE_ASCII_NAME), ASCII)

    #14
    # I.1 + II.5 + III.2) TextLoader 생성자 옳은 파일 이름 입력 + private _getFileEncoding(잘못된 파일)
    def test_get_newWrongReg_encoding_privFunc_when_class_create(self):
        tL = TextLoader(FILE_UTF8_NAME)
        self.assertRaises(Exception, tL._getFileEncoding, WRONG_FILE_NAME)

    # I.1 + II.1 + III.2) TextLoader 생성 시 파일 이름 입력했을 때, _getFileEncoding() / UTF8
    # Case10 과 동일

    #15
    # I.1 + II.1 + III.2) TextLoader 생성 시 파일 이름 입력 안 했을 때, _getFileEncoding(file) / UTF8
    def test_get_right_encoding_UTF8_privFunc_when_not_set_class_create(self):
        tL = TextLoader()
        self.assertEqual(tL._getFileEncoding(FILE_UTF8_NAME), UTF8)

    #16
    # I.2 + II.1 + III.2) TextLoader 생성 이후에 옳은 파일 이름 setFile(), _getFileEncoding() / UTF8
    def test_get_right_encoding_UTF8_privFunc_when_setFile_after_class_create(self):
        tL = TextLoader()
        tL.setFile(FILE_UTF8_NAME)
        self.assertEqual(tL._getFileEncoding(), UTF8)

    #17
    # I.2 + II.1 + III.2) TextLoader 생성 이후에 setFile() 파일 변경, _getFileEncoding() / UTF8
    def test_get_right_encoding_UTF8_privFunc_when_change_setFile(self):
        tL = TextLoader(FILE_ASCII_NAME)
        tL.setFile(FILE_UTF8_NAME)
        self.assertEqual(tL._getFileEncoding(), UTF8)

    #18
    # I.3 + II.1 + III.2)  TextLoader 생성 이후에 함수 자체에서 _getFileEncoding(file) / UTF8
    def test_get_right_encoding_UTF8_privFunc_when_set_funcSelf(self):
        tL = TextLoader(FILE_ASCII_NAME)
        self.assertEqual(tL._getFileEncoding(FILE_UTF8_NAME), UTF8)

    #19
    # I.1 + II.2 + III.2) TextLoader 생성 시 파일 이름 입력했을 때, _getFileEncoding() / ASCII
    def test_get_right_encoding_ASCII_privFunc_when_class_create(self):
        tL = TextLoader(FILE_ASCII_NAME)
        self.assertEqual(tL._getFileEncoding(), ASCII)

    # I.1 + II.2 + III.2) TextLoader 생성 시 파일 이름 입력 안 했을 때, _getFileEncoding(file) / ASCII
    # Case13 과 동일

    #20
    # I.2 + II.2 + III.2) TextLoader 생성 이후에 옳은 파일 이름 setFile(), _getFileEncoding() / ASCII
    def test_get_right_encoding_ASCII_privFunc_when_setFile_after_class_create(self):
        tL = TextLoader()
        tL.setFile(FILE_ASCII_NAME)
        self.assertEqual(tL._getFileEncoding(), ASCII)

    #21
    # I.2 + II.2 + III.2) TextLoader 생성 이후에 setFile() 파일 변경, _getFileEncoding() / ASCII
    def test_get_right_encoding_ASCII_privFunc_when_change_setFile(self):
        tL = TextLoader(FILE_UTF8_NAME)
        tL.setFile(FILE_ASCII_NAME)
        self.assertEqual(tL._getFileEncoding(), ASCII)

    # I.3 + II.2 + III.2)  TextLoader 인자 있게 생성 이후에 함수 자체에서 _getFileEncoding(file) / ASCII
    # Case11 과 동일

    # I.3 + II.2 + III.2)  TextLoader 인자 없이 생성 이후에 함수 자체에서 _getFileEncoding(file) / ASCII
    # Case13 과 동일

    #22
    # I.1 + II.3 + III.2) 빈 파일을 열 때 / UTF8
    def test_get_encoding_UTF8_privFunc_when_open_empty_file(self):
        tL = TextLoader(FILE_EMPTY_UTF8_NAME)
        self.assertEqual(tL._getFileEncoding(), UTF8)

    #23
    # I.1 + II.4 + III.2) 빈 파일은 ASCII -> UTF8로 자동 변환됨
    def test_get_encoding_ASCII_privFunc_when_open_empty_file(self):
        tL = TextLoader(FILE_EMPTY_ASCII_NAME)
        self.assertEqual(tL._getFileEncoding(), UTF8)


    # Get Encoding Test :: method : getEncodingFormat()
    # *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
    #24
    # I.1 + II.1 + III.2) TextLoader 생성자 옳은 파일 이름 입력 + method getEncodingFormat()
    def test_get_encoding_method_when_class_create(self):
        tL = TextLoader(FILE_UTF8_NAME)
        self.assertEqual(tL.getEncodingFormat(), UTF8)

    #25
    # I.1 + II.2 + III.2) TextLoader 생성자 옳은 파일 이름 입력 + method getEncodingFormat(other file)
    def test_get_newReg_encoding_method_when_class_create(self):
        tL = TextLoader(FILE_UTF8_NAME)
        self.assertEqual(tL.getEncodingFormat(FILE_ASCII_NAME), ASCII)

    #26
    # I.1 + II.5 + III.2) TextLoader 생성자 파일 이름 입력 안함 + method getEncodingFormat()
    def test_get_encoding_method_when_not_set_filename_ever(self):
        tL = TextLoader()
        self.assertRaises(Exception, tL.getEncodingFormat)

    #27
    # I.1 + II.2 + III.2) TextLoader 생성자 파일 이름 입력 안함 + method getEncodingFormat(file)
    def test_get_newReg_encoding_method_when_not_set_class_create(self):
        tL = TextLoader()
        self.assertEqual(tL.getEncodingFormat(FILE_ASCII_NAME), ASCII)

    #28
    # I.1 + II.5 + III.2) TextLoader 생성자 옳은 파일 이름 입력 + method getEncodingFormat(잘못된 파일)
    def test_get_newWrongReg_encoding_method_when_class_create(self):
        tL = TextLoader(FILE_UTF8_NAME)
        self.assertRaises(Exception, tL.getEncodingFormat, WRONG_FILE_NAME)

    # I.1 + II.1 + III.2) TextLoader 생성 시 파일 이름 입력했을 때, getEncodingFormat() / UTF8
    # Case24 과 동일

    #29
    # I.1 + II.1 + III.2) TextLoader 생성 시 파일 이름 입력 안 했을 때, getEncodingFormat(file) / UTF8
    def test_get_right_encoding_UTF8_method_when_not_set_class_create(self):
        tL = TextLoader()
        self.assertEqual(tL.getEncodingFormat(FILE_UTF8_NAME), UTF8)

    #30
    # I.2 + II.1 + III.2) TextLoader 생성 이후에 옳은 파일 이름 setFile(), getEncodingFormat() / UTF8
    def test_get_right_encoding_UTF8_method_when_setFile_after_class_create(self):
        tL = TextLoader()
        tL.setFile(FILE_UTF8_NAME)
        self.assertEqual(tL.getEncodingFormat(), UTF8)

    #31
    # I.2 + II.1 + III.2) TextLoader 생성 이후에 setFile() 파일 변경, getEncodingFormat() / UTF8
    def test_get_right_encoding_UTF8_method_when_change_setFile(self):
        tL = TextLoader(FILE_ASCII_NAME)
        tL.setFile(FILE_UTF8_NAME)
        self.assertEqual(tL.getEncodingFormat(), UTF8)

    #32
    # I.3 + II.1 + III.2)  TextLoader 생성 이후에 함수 자체에서 getEncodingFormat(file) / UTF8
    def test_get_right_encoding_UTF8_method_when_set_funcSelf(self):
        tL = TextLoader(FILE_ASCII_NAME)
        self.assertEqual(tL.getEncodingFormat(FILE_UTF8_NAME), UTF8)

    #33
    # I.1 + II.2 + III.2) TextLoader 생성 시 파일 이름 입력했을 때, getEncodingFormat() / ASCII
    def test_get_right_encoding_ASCII_method_when_class_create(self):
        tL = TextLoader(FILE_ASCII_NAME)
        self.assertEqual(tL.getEncodingFormat(), ASCII)

    # I.1 + II.2 + III.2) TextLoader 생성 시 파일 이름 입력 안 했을 때, getEncodingFormat(file) / ASCII
    # Case27 과 동일

    #34
    # I.2 + II.2 + III.2) TextLoader 생성 이후에 옳은 파일 이름 setFile(), getEncodingFormat() / ASCII
    def test_get_right_encoding_ASCII_method_when_setFile_after_class_create(self):
        tL = TextLoader()
        tL.setFile(FILE_ASCII_NAME)
        self.assertEqual(tL.getEncodingFormat(), ASCII)

    #35
    # I.2 + II.2 + III.2) TextLoader 생성 이후에 setFile() 파일 변경, getEncodingFormat() / ASCII
    def test_get_right_encoding_ASCII_method_when_change_setFile(self):
        tL = TextLoader(FILE_UTF8_NAME)
        tL.setFile(FILE_ASCII_NAME)
        self.assertEqual(tL.getEncodingFormat(), ASCII)

    # I.3 + III.2)  TextLoader 인자 있게 생성 이후에 함수 자체에서 getEncodingFormat(file) / ASCII
    # Case25 과 동일

    # I.3 + III.2)  TextLoader 인자 없이 생성 이후에 함수 자체에서 getEncodingFormat(file) / ASCII
    # Case27 과 동일

    #36
    # 빈 파일을 열 때 / UTF8
    def test_get_encoding_UTF8_method_when_open_empty_file(self):
        tL = TextLoader(FILE_EMPTY_UTF8_NAME)
        self.assertEqual(tL.getEncodingFormat(), UTF8)

    #37
    # 빈 파일은 ASCII -> UTF8로 자동 변환됨
    def test_get_encoding_ASCII_method_when_open_empty_file(self):
        tL = TextLoader(FILE_EMPTY_ASCII_NAME)
        self.assertEqual(tL.getEncodingFormat(), UTF8)

    #??
    def test_encoding_read_wrong_file_read(self):
        if os.path.isfile('TestFile_ASCII.txt'):
            tL = TextLoader('TestFile_ASCII.txt')
            self.assertIsNotNone(tL.loadListFromFile())

    # Get Encoding Test :: overloading Func : getEncodingFormat
    # *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
    #38
    # I.3 + II.1 + III.2 ) 오버로딩 외부 함수에서 인코딩 읽기 / UTF8
    def test_get_encoding_UTF8_overloading(self):
        self.assertEqual(getEncodingFormat(FILE_UTF8_NAME), UTF8)

    #39
    # I.3 + II.2 + III.2 ) 오버로딩 외부 함수에서 인코딩 읽기 / ASCII
    def test_get_encoding_ASCII_overloading(self):
        self.assertEqual(getEncodingFormat(FILE_ASCII_NAME), ASCII)

    #40
    # 빈 파일을 열 때 / UTF8
    def test_get_encoding_UTF8_overloading_when_open_empty_file(self):
        self.assertEqual(getEncodingFormat(FILE_EMPTY_UTF8_NAME), UTF8)

    #41
    # 빈 파일은 ASCII -> UTF8로 자동 변환됨
    def test_get_encoding_ASCII_overloading_when_open_empty_file(self):
        self.assertEqual(getEncodingFormat(FILE_EMPTY_ASCII_NAME), UTF8)

    #42
    def test_get_encoding_when_wrong_file_register(self):
        self.assertRaises(Exception, getEncodingFormat, WRONG_FILE_NAME)

    #43
    def test_isInstance_setTextLoader_none_set_filename(self):
        self.assertIsInstance(setTextLoader(), TextLoader)

    #44
    def test_isInstance_setTextLoader_set_filename(self):
        self.assertIsInstance(setTextLoader(FILE_UTF8_NAME), TextLoader)

    #45
    def test_get_filename_after_setTextLoader_set_filename(self):
        self.assertEqual(setTextLoader(FILE_UTF8_NAME).getFileName(), FILE_UTF8_NAME)

    #46
    def test_get_filename_after_setTextLoader_not_set_filename(self):
        self.assertIsNone(setTextLoader().getFileName())

    #47
    def test_get_encoding_after_setTextLoader_set_filename(self):
        self.assertEqual(setTextLoader(FILE_UTF8_NAME).getEncodingFormat(), UTF8)

    #48
    def test_get_encoding_after_setTextLoader_not_set_filename(self):
        self.assertRaises(Exception, setTextLoader().getEncodingFormat)

    #49
    def test_get_list_encoding_UTF8_in_class_when_set_filename_init(self):
        tL = TextLoader(FILE_UTF8_NAME)
        self.assertEqual(tL.loadListFromFile(), TEST_TXT_LIST)

    #50
    def test_get_list_encoding_ASCII_in_class_when_set_filename_init(self):
        tL = TextLoader(FILE_ASCII_NAME)
        self.assertEqual(tL.loadListFromFile(), TEST_TXT_LIST)

    #51
    def test_get_list_encoding_UTF8_in_class_when_set_filename_init_empty(self):
        tL = TextLoader(FILE_EMPTY_UTF8_NAME)
        self.assertEqual(tL.loadListFromFile(), EMPTY_TXT_LIST)

    #52
    def test_get_list_encoding_ASCII_in_class_when_set_filename_init_empty(self):
        tL = TextLoader(FILE_EMPTY_ASCII_NAME)
        self.assertEqual(tL.loadListFromFile(), EMPTY_TXT_LIST)

    #53
    def test_get_right_list_UTF8_when_not_set_file_init(self):
        self.assertEqual(TextLoader().loadListFromFile(FILE_UTF8_NAME), TEST_TXT_LIST)

    #54
    def test_get_right_list_ASCII_when_not_set_file_init(self):
        self.assertEqual(TextLoader().loadListFromFile(FILE_ASCII_NAME), TEST_TXT_LIST)

    #55
    def test_get_none_list_when_TextLoader_not_set_filename_ever(self):
        self.assertIsNone(TextLoader().loadListFromFile())

    #56
    def test_get_raise_when_loadListFromFile_not_set_filename_ever(self):
        self.assertRaises(Exception, loadListFromFile)

    #57
    def test_get_raise_getEncodingFormat_set_none_param(self):
        self.assertRaises(Exception, getEncodingFormat)

    #58
    def test_get_right_list_UTF8_overloading(self):
        self.assertEqual(loadListFromFile(FILE_UTF8_NAME), TEST_TXT_LIST)

    #59
    def test_get_right_list_ASCII_overloading(self):
        self.assertEqual(loadListFromFile(FILE_ASCII_NAME), TEST_TXT_LIST)

    #60
    def test_get_raises_loadListFromFile_when_set_wrong_file(self):
        self.assertRaises(Exception, loadListFromFile, WRONG_FILE_NAME)

    #61
    def test_get_empty_list_UTF8_overloading(self):
        self.assertEqual(loadListFromFile(FILE_EMPTY_UTF8_NAME), EMPTY_TXT_LIST)

    #62
    def test_get_empty_list_ASCII_overloading(self):
        self.assertEqual(loadListFromFile(FILE_EMPTY_ASCII_NAME), EMPTY_TXT_LIST)

if __name__ == '__main__':
    unittest.main()
