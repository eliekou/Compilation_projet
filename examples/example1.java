class Factorial{
    public static void main(String[] a){
        System.out.println(new Fac().ComputeFac(10));
    }
}

class Fac {
    public int ComputeFac(int num){
        int num_aux ;
        if (num < 1)
            num_aux = 1 ;
        else
            num_aux = num * (this.ComputeFac(num-1)) ;
        return num_aux ;
    }
}

"""// MainClass ::= "class" "MainClass" "{" "public" "static" "void" "main" 
//                 "(" "String" "[" "]" "args" ")" "{" "}" "}"
class MainClass {  
    public static void main(String[] args) {  
        a = 1;

    }  
}
#D'abord parse les mainclass avec 1 seule statement
#parse_if statement
#parse_while
#parse"""