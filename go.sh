MYBASE=$(pwd)
# cosmos-sdk
protoc --proto_path=$MYBASE/cosmos-sdk/proto --proto_path=$MYBASE/cometbft/proto --proto_path=$MYBASE/api-common-protos --proto_path=$MYBASE/gogoproto --proto_path=$MYBASE/cosmos-proto/proto --python_out=$MYBASE/generated $(find $MYBASE/cosmos-sdk/proto/amino/ -name '*.proto')
protoc --proto_path=$MYBASE/cosmos-sdk/proto --proto_path=$MYBASE/cometbft/proto --proto_path=$MYBASE/api-common-protos --proto_path=$MYBASE/gogoproto --proto_path=$MYBASE/cosmos-proto/proto --python_out=$MYBASE/generated $(find $MYBASE/cosmos-sdk/proto/cosmos/ -name '*.proto')


# ethermint
protoc --proto_path=$MYBASE/ethermint/proto --proto_path=$MYBASE/cosmos-proto/proto --proto_path=$MYBASE/api-common-protos --proto_path=$MYBASE/gogoproto --proto_path=$MYBASE/cosmos-sdk/proto --python_out=$MYBASE/generated $(find $MYBASE/ethermint/proto/ethermint/ -name '*.proto')

# gogo proto
protoc --proto_path=$MYBASE/gogoproto --python_out=$MYBASE/generated $(find $MYBASE/gogoproto/gogoproto -name '*.proto')

# cosmos-proto
protoc --proto_path=$MYBASE/cosmos-proto/proto --proto_path=$MYBASE/api-common-protos --proto_path=$MYBASE/gogoproto  --python_out=$MYBASE/generated $MYBASE/cosmos-proto/proto/cosmos_proto/cosmos.proto

# cometbft
protoc --proto_path=$MYBASE/cometbft/proto --proto_path=$MYBASE/gogoproto --python_out=$MYBASE/generated $(find $MYBASE/cometbft/proto/cometbft -name '*.proto')

