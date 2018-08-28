### String
> Redis 的最基本类型， 最大能存储512M的数据，String是二进制安全的， 可以存储任意书数据， 图片 数字 序列化对象等
+ 设置
    + 设置键值 `set key value`
    + 设置键值和过期时间(s),超时自动删除 `setex key seconds value`
    + 设置多个键值 `mset key value key value ...`
+ 获取
    + 根据key获取值， 不存在返回None(null 0 nil) `get key`
    + mget key key key
+ 运算 *值是字符型串型的数字*
	+ 将key对应的值加1 `incr key`
	+ 将key对应得值减1 `decr key`
	+ 将key对应的值加整数 `incrby key intnum`
	+ 将key对应的值减整数 `decrby key intnum`
+ 其他
	+ 追加值
	+ 
