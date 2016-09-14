**Reference:** https://github.com/happynear/caffe-windows

I just apply to inference term, removing backward algorithm to release mode.
If you want to use debug mode project, you have to set up debug 3rdparty library.

## Usage step:

1. Run ./build_cpu_only/MainBuilder.sln

2. Compile mode : Release and x64

3. Look at the classification.cpp in caffe project
 - argv[1] : caffe cnn layer architecture
 - argv[2] : dumped model e.g) linux gpu caffe learning model, lenet_iter_3622.caffemodel
 - argv[3] : test image, format is jpg and png, which opencv imread input 
 
4. Compile : first caffelib and then caffe project
 - caffelib make ./bin/caffelib.lib
 - caffe make ./bin/caffe.exe -> it is execute file

5. CPU mode shallow build.

### Example

open cmd 

1. cd ./example_face_feature/caffe.exe 

2. caffe.exe siamese_test-leveldb_10layer.prototxt total_iter_222000.caffemodel _onejinimage_0009.png

3. output is 13dimension CNN feature output

### Python example verification

1. cd ./example_Face_verification

2. execute python script : python caffe_cnn.py ./Test/image_0022.png

3. you can see score name list, which alread enroll in function.py