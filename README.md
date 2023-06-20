# Web_page
 Using Python(flask) and html and javascript to fetch data from SQL Server and display it as a web page
 PYTHON FLASK <--> IIS connect Local_Sever
__pycache__ 폴더:

이 폴더는 Python 파일이 컴파일된 후 생성되는 캐시 파일들을 저장하는 곳입니다.
Python 인터프리터는 코드를 실행하기 전에 해당 코드를 컴파일하여 바이트 코드로 변환합니다. 컴파일된 바이트 코드는 __pycache__ 폴더에 저장되며, 이를 통해 같은 모듈이 다시 로드될 때 컴파일 단계를 건너뛰고 캐시된 바이트 코드를 사용할 수 있습니다.

env 폴더:
env 폴더는 프로젝트의 가상 환경(Virtual Environment)을 포함하는 폴더입니다.
가상 환경은 Python 프로젝트를 독립된 환경에서 실행하기 위해 사용되며, 프로젝트에 필요한 패키지들을 격리된 공간에 설치하고 사용할 수 있게 해줍니다.
env 폴더에는 가상 환경 설정과 필요한 패키지들이 포함되어 있습니다.
static 폴더:

static 폴더는 웹 애플리케이션에서 사용되는 정적 파일들을 저장하는 폴더입니다.
정적 파일은 CSS, JavaScript, 이미지 등과 같이 서버에서 동적으로 생성되지 않고, 브라우저에 직접 제공되는 파일입니다.
웹 페이지에서 사용되는 스타일 시트, 스크립트 파일, 이미지 등을 static 폴더에 저장하여 웹 애플리케이션에서 사용할 수 있습니다.

templates/main 폴더:
templates/main 폴더는 Flask 웹 애플리케이션에서 사용되는 HTML 템플릿 파일을 저장하는 폴더입니다.
HTML 템플릿은 동적으로 생성된 컨텐츠를 포함하는 웹 페이지를 작성할 때 사용됩니다.
templates/main 폴더에는 주로 공통 레이아웃, 부분적인 템플릿 등이 저장됩니다.

list.html 파일:
list.html 파일은 templates/main 폴더에 위치한 HTML 템플릿 파일입니다.
이 파일은 Flask 웹 애플리케이션에서 사용되는 특정 페이지의 뷰를 구성하는 HTML 코드가 포함되어 있습니다.
list.html 파일은 사용자에게 데이터 목록을 표시하거나 동적으로 생성된 내용을 템플릿에 렌더링

app.py 파일은 Flask 웹 애플리케이션의 메인 파일입니다. 이 파일은 웹 애플리케이션의 라우팅, 비즈니스 로직, 데이터 처리 등을 담당합니다. Flask 프레임워크를 사용하여 웹 애플리케이션을 구축할 때 일반적으로 app.py 파일을 생성하고 여기에 필요한 라우트(경로)와 뷰 함수(페이지 처리 로직)를 작성합니다.

web.config 파일은 Microsoft IIS (Internet Information Services) 웹 서버에서 실행되는 ASP.NET 애플리케이션을 구성하는 설정 파일입니다. 이 파일은 IIS에게 웹 애플리케이션을 어떻게 처리할지 알려주는 역할을 합니다. Flask 애플리케이션을 IIS에서 호스팅하고자 할 때, web.config 파일을 사용하여 IIS 서버와 Flask 애플리케이션 간의 통신을 설정할 수 있습니다.

wfastcgi.py 파일은 FastCGI 프로토콜을 지원하는 웹 서버와 Flask 애플리케이션을 연결하는 데 사용되는 FastCGI 서버입니다. FastCGI는 웹 서버와 애플리케이션 사이에서 웹 요청을 처리하는 데 사용되는 프로토콜입니다. wfastcgi.py 파일은 Flask 애플리케이션을 FastCGI 서버로 실행시키고, 웹 서버와 통신하며 요청을 처리하는 역할을 합니다.

일반적인 구성은 다음과 같습니다:

웹 서버 (예: IIS)는 web.config 파일을 읽어 Flask 애플리케이션과의 통신을 설정합니다.
wfastcgi.py 파일은 FastCGI 서버로서 동작하여 웹 서버와 통신하고, Flask 애플리케이션으로부터 받은 요청을 처리합니다.
app.py 파일은 Flask 애플리케이션의 메인 파일로서 웹 애플리케이션의 라우팅과 뷰 함수 등을 정의합니다.
Flask 애플리케이션은 app.py 파일을 실행하여 웹 요청을 처리하고 응답을 생성합니다.
이렇게 함으로써, web.config, wfastcgi.py, app.py 파일을 함께 사용하여 Flask 애플리케이션을 IIS에서 실행하고 웹 요청을 처리할 수 있습니다.

돌아가는 로직에 대해 알고 싶으면 FLASK.docx파일을 열어서 확인해 보세요. 정리해 뒀습니다
잘못된 점이나 문제가 있으면 알려주세요
