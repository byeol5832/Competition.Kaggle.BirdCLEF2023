import json

class UserSecretsClient:
    '''
    이 Class는 kaggle notebook의 secret을 모방합니다.
    기존 kaggle code의 wandb 코드를 local에서 그대로 사용하기 위해 구현되었습니다.

    작성자 : 404Vector
    '''
    def __init__(self) -> None:
        file_path = './secret.json' # 고정 값 입니다.
        with open(file_path, 'r') as file:
            self.json = json.load(file)

    def get_secret(self, key):
        return self.json[key]