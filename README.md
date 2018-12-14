# **json2struct**



> 此脚本主要用于快速把json结果变成struct的定义。使用 vscode 进行修改 `s_json` 进行快速适配你所要转换的json.



- [x] 此脚本基于 `python 2.7.x` 的语法所写, 与 `python 3` 的语法不兼容

例子:

```json
{
        "data" : {
            "order_id" : "b2db6bf74e124874ac4d1c0154f33a42",
            "paytransaction_id" : "81020171114182945417671878656102"
        },
        "ret_code" : 8000001,
        "ret_float" : 2.36,
        "list": [{"name":"1", "val": 2}],
        "list_int": [2,3],
        "param":{
            "list": [{"name":"1", "val": 2, "ll":[2,2.1]}],
            "list_int": [2,3],
            "code" : 8000001,
            "ext":{
                "name": "1001"
            }
        },
        "ret_msg" : "DD200207;交易处理中!"
}
```



自动生成结果:

```go
type st_resp_list struct {
	Name string `json:"name"`
	Val  int    `json:"val"`
}

type st_resp_param_list struct {
	Ll   []float32 `json:"ll"`
	Name string    `json:"name"`
	Val  int       `json:"val"`
}

type st_resp_param_ext struct {
	Name string `json:"name"`
}

type st_resp_param struct {
	List_int []int                 `json:"list_int"`
	Code     int                   `json:"code"`
	List     []*st_resp_param_list `json:"list"`
	Ext      *st_resp_param_ext    `json:"ext,omitempty"`
}

type st_resp_data struct {
	Order_id          string `json:"order_id"`
	Paytransaction_id string `json:"paytransaction_id"`
}

type st_resp struct {
	Ret_code  int             `json:"ret_code"`
	List      []*st_resp_list `json:"list"`
	Param     *st_resp_param  `json:"param,omitempty"`
	List_int  []int           `json:"list_int"`
	Ret_msg   string          `json:"ret_msg"`
	Data      *st_resp_data   `json:"data,omitempty"`
	Ret_float float32         `json:"ret_float"`
}
```



再修改下struct的名字即可