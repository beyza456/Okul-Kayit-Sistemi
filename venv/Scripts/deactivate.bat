REM -----------------------------------------------------------------------------
REM Bu dosya, projenin sanal Python ortamını (virtual environment) Windows ortamında devre dışı bırakmak (çıkmak) için kullanılır.
REM Çalıştırıldığında, ortam değişkenleri eski haline döner ve sanal ortam kapatılır.
REM -----------------------------------------------------------------------------

@echo off

if defined _OLD_VIRTUAL_PROMPT (
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
)
set _OLD_VIRTUAL_PROMPT=


if defined _OLD_VIRTUAL_PYTHONHOME (
    set "PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%"
    set _OLD_VIRTUAL_PYTHONHOME=
)


if defined _OLD_VIRTUAL_PATH (
    set "PATH=%_OLD_VIRTUAL_PATH%"
)

set _OLD_VIRTUAL_PATH=

set VIRTUAL_ENV=
set VIRTUAL_ENV_PROMPT=

:END
