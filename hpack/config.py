import os

class Config:
    # 服务器配置
    DeployDomain = 'localhost:8000'
    BaseURL = f"http://{DeployDomain}"

    # 应用信息
    AppIcon = f"{BaseURL}/AppIcon.png"
    AppName = 'emptyharmony'
    Badge = '测试版'
    IndexTemplate = "default"

    # 签名配置
    Alias = 'bieming'
    KeyPwd = 'Abcd@123456'
    KeystorePwd = 'Abcd@123456'

    SignDir = 'sign'
    Cert = os.path.join(SignDir, 'release.cer')
    Profile = os.path.join(SignDir, 'test_release.p7b')
    Keystore = os.path.join(SignDir, 'harmony.p12')

    Debug = True