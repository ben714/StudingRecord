class CD {
    int r;
    CD(int r){
        this.r=r;
    }
}

class DVD extends CD{
    int c;
    DVD(int r,int c){
        super(r);
        this.c=c;
    }
}

public class MyClass{
    public static void main(String[] args){
        int r=1;
        int c=2;
        DVD obj = new DVD(r,c);
    }
}
