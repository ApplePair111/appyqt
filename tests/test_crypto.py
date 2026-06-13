import appyqt.cryptographyTools as crypto

def test_passtoferkey():
    assert crypto.password_to_fernet_key("test", "abcdef".encode()) == b"-8_sPw5KaguDRRPbAa8DhZVyfAgB3pfxrQqY4GsSQOs="

def test_passtoferkeyNosalt():
    assert crypto.password_to_fernet_key_nosalt("test") == b'4v6egGHvoQ4Hyy3b8x7-ctUZOJnvhME4P8OaZXydSvg='

def test_encrypt():
    assert crypto.pwdDecrypt("test", crypto.pwdEncrypt("test", "testtesttest")) == "testtesttest".encode()

def test_decrypt():
    assert crypto.pwdDecrypt("test", b'gAAAAABqLPVLn12qCnTa1AOpeoCQVtSXPXL0Ezr1mNORMRuiq7Tg2O0_OBS34pdEfltCpS2_qtrWwiXcl9swy0hKdoRbPSZwvw==') == "testtesttest".encode()