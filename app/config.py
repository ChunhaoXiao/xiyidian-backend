from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    appid:str = "wx282a4265599d53a0" 
    app_secret:str = "8ad8fd6d476ef17d27eea8111af65e2c"

settings = Settings()