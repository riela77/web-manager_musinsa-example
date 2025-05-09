# web-manager_musinsa-example
making web which belonging with DB,  fastapi, jQuery, web browser

해당 예시는 **MVC 패턴**과 **백엔드-프론트엔드 분리 구조**를 기반으로 하고 있다. 
---

### 🔴 **Oracle DB**

* 데이터베이스 역할.
* 데이터 저장 및 검색을 담당.

---

### 🟢 **Uvicorn + FastAPI (백엔드 서버)**

* **Uvicorn**은 ASGI 서버로서 FastAPI 앱을 실행시킴.
* **FastAPI**는 백엔드 프레임워크로, 클라이언트(프론트엔드)의 요청을 처리.
* 내부적으로 **MVC 패턴** 중 \*\*M (Model)\*\*과 **C (Controller)** 부분을 담당:

  * **M (Model)**: DB와 연결하여 데이터 처리.
  * **C (Controller)**: HTTP 요청을 받아 로직을 처리하고, 데이터를 반환.

---

### 🔵 **Tomcat + jQuery (프론트엔드 서버)**

* **Tomcat**은 Java 기반의 WAS(Web Application Server)로 HTML, JS 등을 클라이언트에 제공.
* **jQuery**는 JavaScript 라이브러리로, 사용자와의 상호작용 처리 및 Ajax 요청에 활용.
* 여기서는 **V (View)** 역할:

  * 사용자에게 보여지는 화면 구성.
  * Ajax 등을 통해 FastAPI에 데이터 요청 및 결과 표시.

---

### ⚫ **사용자 (웹 브라우저)**

* 최종 사용자.
* 웹 브라우저로 Tomcat 서버에 접속하여 jQuery 기반 화면을 보고 조작.
* jQuery가 백엔드(FastAPI)와 비동기 통신하여 화면을 갱신.

---

### 🔄 **전체 흐름 요약**

1. 사용자가 웹 브라우저를 통해 Tomcat에 접속.
2. Tomcat이 HTML/JS (jQuery 포함)를 사용자에게 전달.
3. 사용자의 조작 → jQuery가 Ajax로 FastAPI에 요청.
4. FastAPI (Uvicorn)는 Controller → Model → Oracle DB를 통해 데이터 처리.
5. 처리 결과가 다시 jQuery로 전달되어 화면(View)에 표시됨.

