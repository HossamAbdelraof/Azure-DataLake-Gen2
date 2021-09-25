# Azure-DataLake-Gen2
manage Azure DataLake Gen 2 with python 


first install required libraries 

```python
pip install azure-storage-file-datalake
```

this python file provide important actions with azure Blob storage (DataLAke Gen2)

* here will manage directories (navigation, create, rename, delate)
* working with files(upload text file, upload big file)

## First 
import libraries

```python
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core.exceptions import ResourceExistsError
```

### authorication 

Create Service Client 

```python
Storage_Account_url = "https://{Storate_Account_Name}.dfs.core.windows.net/"

Storage_Account_credential = '{Access_Key}'

DataLake_service = DataLakeServiceClient(account_url = Storage_Account_url,
                   credential = Storage_Account_credentiall)

```



## 1- manage directories

##### 1.1 create file systems 
to create 

```python
  File_Sistem_Client = DataLake_service.create_file_system(file_system = {File_System_Name})
```
> this code create file system with name of: {File_System_Name}
>  replace {File_System_Name} with any other name

 to load existing file system 
 ```python
  File_Sistem_Client = datalake_service.get_file_system_client( {File_System_Name} )
 ```
 > this code will load an existing fileSystem (container) with the name: {File_System_Name}

#####1.1.2 Directories
create directories we must use 
 ```python
 Directory_Client = File_Sistem_Client.create_directory("my-directory")
  ```
  > the directorise must be inside File system so we use current file system client (File_Sistem_Client) \n
  > teh directory can be any number of folders like: " folder1\folder2\folder3 "

we can consider teh directory is child of File System and we can access teh child only of oyher directories 
```python
 Directory_Client  = File_Sistem_Client.get_directory_client(" folder1\folder2 ")
 Directory_Client = Directory_Clien.get_directory_client(" folder3 ")
```


the storaget account name is 
"http://{storage_account_name}.dfs.core.windows.net"

credential = "access key"
}{POIUYTRE":LKJHGFDSA?><MNBVCCCCXZ/.,mnbvcxz';lkjhgfdssssssssa][poiuytrewq=-0987654321+_)(*&^%$#@

