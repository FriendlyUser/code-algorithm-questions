function sqrtDouble(number) {
    var threshold = 0.1;
    //9 try middle,
    var upper = number;
    var lower = 0;
    var middle;
    while(upper-lower>threshold){
        middle = (upper+lower)/2;
        if(middle*middle>number){
            upper = middle;
        }else{
            lower = middle;
        }
    }
    return middle
}