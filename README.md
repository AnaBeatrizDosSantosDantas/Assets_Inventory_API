## README (Versão em Português)

# API de Inventário de Ativos de TI

# Lista de Rotas da API

Rota: /employees/  
Função: CRUD dos funcionários

Rota: /employees/{cpf}  
Função: CRUD do inventário de um funcionário

Rota: /assets/  
Função: Lista todos os ativos

Rota: /assets/{asset_type}  
Função: CRUD dos dados de um ativo

Rota: /assets/{asset_type}/{cpf}  
Função: CRUD dos dados de um ativo a um funcionário específico

## Instalação

1. Clone o repositório:

    ```bash
    git clone <url-do-repositorio> # ou baixe o diretório em .zip
    ```

2. Crie um ambiente virtual e instale as dependências:

    ```bash
    cd <nome-do-diretorio>
    python -m venv venv
    source venv/Scripts/activate  # No Windows, use `.\venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Certifique-se de que o MongoDB está rodando na sua máquina local ou em um servidor acessível.

4. Execute a aplicação:
    ```bash
    python app.py
    ```

## Utilização

## Guia do Postman

1. Instale o Postman: [Download Postman](https://www.postman.com/downloads/)

2. Abra o Postman e clique em `New` para criar uma nova requisição.

3. Selecione o método apropriado (GET, POST, PUT, DELETE) conforme listado acima para cada endpoint.

4. Insira a URL da API conforme especificado.

5. Se a requisição requer um corpo JSON (para métodos POST e PUT), selecione a aba `Body`, escolha `raw` e `JSON`, e insira o JSON apropriado.

6. Clique em `Send` para enviar a requisição.

7. Verifique a resposta da API na seção `Response` do Postman.

### Exemplo de Requisição no Postman

Para inserir um novo funcionário:

1. Clique em `New` -> `Request`.
2. Selecione o método `POST`.
3. Insira a URL `http://127.0.0.1:5000/employees/`.
4. Vá para a aba `Body`, selecione `raw` e `JSON`.
5. Insira o seguinte JSON:
    ```json
    {
        "cpf": "12345678900",
        "name": "Ana Beatriz"
    }
    ```
6. Clique em `Send`.

Siga este formato para testar todas as rotas listadas na seção "Endpoints".

### Testando as Rotas com Postman

#### Funcionários

##### Inserir um novo funcionário

-   **URL:** `http://127.0.0.1:5000/employees/`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "cpf": "12345678900",
        "name": "Ana Beatriz"
    }
    ```

##### Excluir um funcionário

-   **URL:** `http://127.0.0.1:5000/employees/12345678900`
-   **Método:** `DELETE`

##### Listar todos os funcionários

-   **URL:** `http://127.0.0.1:5000/employees/`
-   **Método:** `GET`

##### Consultar o inventário completo de um determinado funcionário

-   **URL:** `http://127.0.0.1:5000/employees/12345678900`
-   **Método:** `GET`

##### Atualizar o nome do funcionário

-   **URL:** `http://127.0.0.1:5000/employees/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "name": "Ana Beatriz dos Santos Dantas"
    }
    ```

#### Ativos

##### Inserir dados de um ativo notebook

-   **URL:** `http://127.0.0.1:5000/assets/notebook/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1234",
        "model": "ACER",
        "serial_number": "76178231T812",
        "version": "WINDOWS 11 PRO",
        "characteristics": "Intel i7 16GB RAM 512GB SSD \"14",
        "observations": "Possui riscos na tela"
    }
    ```

##### Atualizar as informações do ativo notebook

-   **URL:** `http://127.0.0.1:5000/assets/notebook/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1234",
        "model": "ACER",
        "serial_number": "76178231T814",
        "version": "WINDOWS 11 PRO",
        "characteristics": "Intel i7 16GB RAM 512GB SSD \"14",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo notebook

-   **URL:** `http://127.0.0.1:5000/assets/notebook/12345678900`
-   **Método:** `DELETE`

##### Inserir dados de um ativo monitor 1

-   **URL:** `http://127.0.0.1:5000/assets/monitor1/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "AOC",
        "serial_number": "1242342343",
        "observations": "-"
    }
    ```

##### Atualizar as informações do ativo monitor 1

-   **URL:** `http://127.0.0.1:5000/assets/monitor1/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "AOC",
        "serial_number": "1242342341",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo monitor 1

-   **URL:** `http://127.0.0.1:5000/assets/monitor1/12345678900`
-   **Método:** `DELETE`

##### Inserir dados de um ativo monitor 2

-   **URL:** `http://127.0.0.1:5000/assets/monitor2/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "AOC",
        "serial_number": "1242342342",
        "observations": "-"
    }
    ```

##### Atualizar as informações do ativo monitor 2

-   **URL:** `http://127.0.0.1:5000/assets/monitor2/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "AOC",
        "serial_number": "1242342344",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo monitor 2

-   **URL:** `http://127.0.0.1:5000/assets/monitor2/12345678900`
-   **Método:** `DELETE`

##### Inserir dados de um ativo teclado

-   **URL:** `http://127.0.0.1:5000/assets/teclado/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "41232132",
        "observations": "-"
    }
    ```

##### Atualizar as informações do ativo teclado

-   **URL:** `http://127.0.0.1:5000/assets/teclado/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "41232138",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo teclado

-   **URL:** `http://127.0.0.1:5000/assets/teclado/12345678900`
-   **Método:** `DELETE`

##### Inserir dados de um ativo mouse

-   **URL:** `http://127.0.0.1:5000/assets/mouse/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "12323234",
        "observations": "-"
    }
    ```

##### Atualizar as informações do ativo mouse

-   **URL:** `http://127.0.0.1:5000/assets/mouse/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "12323237",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo mouse

-   **URL:** `http://127.0.0.1:5000/assets/mouse/12345678900`
-   **Método:** `DELETE`

##### Inserir dados de um ativo nobreak

-   **URL:** `http://127.0.0.1:5000/assets/nobreak/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1234",
        "model": "AEM-2024",
        "serial_number": "SN-56789",
        "version": "1.0.0",
        "characteristics": "8-core CPU, 16GB RAM, 512GB SSD, AEM Optimized",
        "observations": "-"
    }
    ```

##### Atualizar as informações do ativo nobreak

-   **URL:** `http://127.0.0.1:5000/assets/nobreak/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1244",
        "model": "AEM-2023",
        "serial_number": "SN-56781",
        "version": "1.0.0",
        "characteristics": "8-core CPU, 32GB RAM, 512GB SSD, AEM Optimized",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo nobreak

-   **URL:** `http://127.0.0.1:5000/assets/nobreak/12345678900`
-   **Método:** `DELETE`

##### Inserir dados de um ativo desktop

-   **URL:** `http://127.0.0.1:5000/assets/desktop/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1234",
        "model": "-",
        "serial_number": "-",
        "version": "-",
        "characteristics": "-",
        "observations": "-"
    }
    ```

##### Atualizar as informações do ativo desktop

-   **URL:** `http://127.0.0.1:5000/assets/desktop/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1232",
        "model": "-",
        "serial_number": "-",
        "version": "-",
        "characteristics": "-",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo desktop

-   **URL:** `http://127.0.0.1:5000/assets/desktop/12345678900`
-   **Método:** `DELETE`

##### Inserir dados de um ativo headset

-   **URL:** `http://127.0.0.1:5000/assets/headset/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "1822321",
        "observations": "-"
    }
    ```

##### Atualizar as informações do ativo headset

-   **URL:** `http://127.0.0.1:5000/assets/headset/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "1822325",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo headset

-   **URL:** `http://127.0.0.1:5000/assets/headset/12345678900`
-   **Método:** `DELETE`

##### Inserir dados de um ativo celular

-   **URL:** `http://127.0.0.1:5000/assets/celular/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "Samsung Galaxy A03",
        "imei1": "19823712895",
        "number": "19982249772",
        "observations": "-"
    }
    ```

##### Atualizar as informações do ativo celular

-   **URL:** `http://127.0.0.1:5000/assets/celular/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "Samsung Galaxy A03",
        "imei1": "19823712892",
        "number": "19982249779",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo celular

-   **URL:** `http://127.0.0.1:5000/assets/celular/12345678900`
-   **Método:** `DELETE`

##### Inserir dados de um ativo acessórios

-   **URL:** `http://127.0.0.1:5000/assets/acessorios/12345678900`
-   **Método:** `POST`
-   **Body (JSON):**
    ```json
    {
        "support": "SIM",
        "mouse_pad": "SIM",
        "observations": "-"
    }
    ```

##### Atualizar as informações do ativo acessórios

-   **URL:** `http://127.0.0.1:5000/assets/acessorios/12345678900`
-   **Método:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "support": "NÃO",
        "mouse_pad": "SIM",
        "observations": "-"
    }
    ```

##### Limpar as informações do ativo acessórios

-   **URL:** `http://127.0.0.1:5000/assets/acessorios/12345678900`
-   **Método:** `DELETE`

##### Listar todos os ativos

-   **URL:** `http://127.0.0.1:5000/assets/`
-   **Método:** `GET`

##### Consultar um ativo de um funcionário específico

-   **URL:** `http://127.0.0.1:5000/assets/<asset_type>/<cpf>`
-   **Método:** `GET`

##README (English Version)

# IT Asset Inventory API

# API Routes List

Route: /employees/  
Function: CRUD operations for employees

Route: /employees/{cpf}  
Function: CRUD operations for an employee's inventory

Route: /assets/  
Function: List all assets

Route: /assets/{asset_type}  
Function: CRUD operations for asset data

Route: /assets/{asset_type}/{cpf}  
Function: CRUD operations for assigning asset data to a specific employee

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <directory-name>
    ```

2. Create a virtual environment and install the dependencies:

    ```bash
    python -m venv venv
    source venv/Scripts/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Ensure that MongoDB is running on your local machine or on an accessible server.

4. Run the application:
    ```bash
    python app.py
    ```

## Usage

## Postman Guide

1. Install Postman: [Download Postman](https://www.postman.com/downloads/)

2. Open Postman and click on `New` to create a new request.

3. Select the appropriate method (GET, POST, PUT, DELETE) as listed above for each endpoint.

4. Enter the API URL as specified.

5. If the request requires a JSON body (for POST and PUT methods), select the `Body` tab, choose `raw` and `JSON`, and enter the appropriate JSON.

6. Click `Send` to send the request.

7. Check the API response in the `Response` section of Postman.

### Example Request in Postman

To add a new employee:

1. Click `New` -> `Request`.
2. Select the method `POST`.
3. Enter the URL `http://127.0.0.1:5000/employees/`.
4. Go to the `Body` tab, select `raw` and `JSON`.
5. Enter the following JSON:
    ```json
    {
        "cpf": "12345678900",
        "name": "Ana Beatriz"
    }
    ```
6. Click `Send`.

Follow this format to test all the routes listed in the "Endpoints" section.

### Testing the Routes with Postman

#### Employees

##### Add a new employee

-   **URL:** `http://127.0.0.1:5000/employees/`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "cpf": "12345678900",
        "name": "Ana Beatriz"
    }
    ```

##### Delete an employee

-   **URL:** `http://127.0.0.1:5000/employees/12345678900`
-   **Method:** `DELETE`

##### List all employees

-   **URL:** `http://127.0.0.1:5000/employees/`
-   **Method:** `GET`

##### Get the complete inventory of a specific employee

-   **URL:** `http://127.0.0.1:5000/employees/12345678900`
-   **Method:** `GET`

##### Update the employee's name

-   **URL:** `http://127.0.0.1:5000/employees/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "name": "Ana Beatriz dos Santos Dantas"
    }
    ```

#### Assets

##### Add notebook asset data

-   **URL:** `http://127.0.0.1:5000/assets/notebook/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1234",
        "model": "ACER",
        "serial_number": "76178231T812",
        "version": "WINDOWS 11 PRO",
        "characteristics": "Intel i7 16GB RAM 512GB SSD \"14",
        "observations": "Screen has scratches"
    }
    ```

##### Update notebook asset data

-   **URL:** `http://127.0.0.1:5000/assets/notebook/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1234",
        "model": "ACER",
        "serial_number": "76178231T816",
        "version": "WINDOWS 11 PRO",
        "characteristics": "Intel i7 16GB RAM 512GB SSD \"14",
        "observations": "Screen has scratches"
    }
    ```

##### Delete notebook asset data

-   **URL:** `http://127.0.0.1:5000/assets/notebook/12345678900`
-   **Method:** `DELETE`

##### Add monitor 1 asset data

-   **URL:** `http://127.0.0.1:5000/assets/monitor1/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "AOC",
        "serial_number": "1242342343",
        "observations": "-"
    }
    ```

##### Update monitor 1 asset data

-   **URL:** `http://127.0.0.1:5000/assets/monitor1/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "AOC",
        "serial_number": "1242342347",
        "observations": "-"
    }
    ```

##### Delete monitor 1 asset data

-   **URL:** `http://127.0.0.1:5000/assets/monitor1/12345678900`
-   **Method:** `DELETE`

##### Add monitor 2 asset data

-   **URL:** `http://127.0.0.1:5000/assets/monitor2/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "AOC",
        "serial_number": "1242342344",
        "observations": "-"
    }
    ```

##### Update monitor 2 asset data

-   **URL:** `http://127.0.0.1:5000/assets/monitor2/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "AOC",
        "serial_number": "1242342341",
        "observations": "-"
    }
    ```

##### Delete monitor 2 asset data

-   **URL:** `http://127.0.0.1:5000/assets/monitor2/12345678900`
-   **Method:** `DELETE`

##### Add keyboard asset data

-   **URL:** `http://127.0.0.1:5000/assets/teclado/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "41232132",
        "observations": "-"
    }
    ```

##### Update keyboard asset data

-   **URL:** `http://127.0.0.1:5000/assets/teclado/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "41232137",
        "observations": "-"
    }
    ```

##### Delete keyboard asset data

-   **URL:** `http://127.0.0.1:5000/assets/teclado/12345678900`
-   **Method:** `DELETE`

##### Add mouse asset data

-   **URL:** `http://127.0.0.1:5000/assets/mouse/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "12323234",
        "observations": "-"
    }
    ```

##### Update mouse asset data

-   **URL:** `http://127.0.0.1:5000/assets/mouse/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "12323239",
        "observations": "-"
    }
    ```

##### Delete mouse asset data

-   **URL:** `http://127.0.0.1:5000/assets/mouse/12345678900`
-   **Method:** `DELETE`

##### Add UPS asset data

-   **URL:** `http://127.0.0.1:5000/assets/nobreak/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1234",
        "model": "AEM-2024",
        "serial_number": "SN-56789",
        "version": "1.0.0",
        "characteristics": "8-core CPU, 16GB RAM, 512GB SSD, AEM Optimized",
        "observations": "-"
    }
    ```

##### Update UPS asset data

-   **URL:** `http://127.0.0.1:5000/assets/nobreak/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1234",
        "model": "AEM-2023",
        "serial_number": "SN-56719",
        "version": "1.0.0",
        "characteristics": "8-core CPU, 32GB RAM, 512GB SSD, AEM Optimized",
        "observations": "-"
    }
    ```

##### Delete UPS asset data

-   **URL:** `http://127.0.0.1:5000/assets/nobreak/12345678900`
-   **Method:** `DELETE`

##### Add desktop asset data

-   **URL:** `http://127.0.0.1:5000/assets/desktop/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1234",
        "model": "-",
        "serial_number": "-",
        "version": "-",
        "characteristics": "-",
        "observations": "-"
    }
    ```

##### Update desktop asset data

-   **URL:** `http://127.0.0.1:5000/assets/desktop/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "tag": "XYZ1239",
        "model": "-",
        "serial_number": "-",
        "version": "-",
        "characteristics": "-",
        "observations": "-"
    }
    ```

##### Delete desktop asset data

-   **URL:** `http://127.0.0.1:5000/assets/desktop/12345678900`
-   **Method:** `DELETE`

##### Add headset asset data

-   **URL:** `http://127.0.0.1:5000/assets/headset/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "1822325",
        "observations": "-"
    }
    ```

##### Update headset asset data

-   **URL:** `http://127.0.0.1:5000/assets/headset/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "LOGITEC",
        "serial_number": "1822321",
        "observations": "-"
    }
    ```

##### Delete headset asset data

-   **URL:** `http://127.0.0.1:5000/assets/headset/12345678900`
-   **Method:** `DELETE`

##### Add mobile phone asset data

-   **URL:** `http://127.0.0.1:5000/assets/celular/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "model": "Samsung Galaxy A03",
        "imei1": "19823712895",
        "number": "19982249772",
        "observations": "-"
    }
    ```

##### Update mobile phone asset data

-   **URL:** `http://127.0.0.1:5000/assets/celular/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "model": "Samsung Galaxy A03",
        "imei1": "19823712892",
        "number": "19982249779",
        "observations": "-"
    }
    ```

##### Delete mobile phone asset data

-   **URL:** `http://127.0.0.1:5000/assets/celular/12345678900`
-   **Method:** `DELETE`

##### Add accessories asset data

-   **URL:** `http://127.0.0.1:5000/assets/acessorios/12345678900`
-   **Method:** `POST`
-   **Body (JSON):**
    ```json
    {
        "support": "YES",
        "mouse_pad": "YES",
        "observations": "-"
    }
    ```

##### Update accessories asset data

-   **URL:** `http://127.0.0.1:5000/assets/acessorios/12345678900`
-   **Method:** `PUT`
-   **Body (JSON):**
    ```json
    {
        "support": "NO",
        "mouse_pad": "YES",
        "observations": "-"
    }
    ```

##### Delete accessories asset data

-   **URL:** `http://127.0.0.1:5000/assets/acessorios/12345678900`
-   **Method:** `DELETE`

##### List all assets

-   **URL:** `http://127.0.0.1:5000/assets/`
-   **Method:** `GET`

##### Get an asset of a specific employee

-   **URL:** `http://127.0.0.1:5000/assets/<asset_type>/<cpf>`
-   **Method:** `GET`
