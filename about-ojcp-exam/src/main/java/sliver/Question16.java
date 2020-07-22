class MissingInfoException extends Exception{}

class AgeOutofRangeException extends Exception{}

class Candidate{
    String name;
    int age;
    Candidate(String name, int age) throws Exception{
        if(name==null){
            throw new MissingInfoException();
        }else if(age<=10 || age>=150){
            throw new AgeOutofRangeException();
        }else{
            this.name=name;
            this.age=age;
        }
    }
    public String toString(){
        return name+" age: "+age;
    }

    //Add throws Exception in main method will work
/*    public static void main(String args[]) throws Exception{
        Candidate c = new Candidate("James",20);
        Candidate c1 = new Candidate("William",35);
        System.out.println(c);
        System.out.println(c1);
    }*/
    
    public static void main(String args[]){
        Candidate c = null;
        Candidate c1 = null;
        try {
          c = new Candidate("James",20);
          c1 = new Candidate("William",35);
        }catch(MissingInfoException e2){}
        catch(AgeOutofRangeException e3){}
        catch(Exception e1){}
        //children first and then the parent exceptions
        System.out.println(c);
        System.out.println(c1);
    }
}
