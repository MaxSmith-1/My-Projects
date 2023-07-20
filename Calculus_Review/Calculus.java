public class Calculus {


    public Calculus(){}


    public String derivitive(Double[] a){


        int b = a.length - 1;
        String answer = "";
        for(double x : a){
            double c = x*b;
            b-=1;
            if(b>-1) {
                answer += String.valueOf(c) + "x^" + String.valueOf(b) + " + ";
            }
            else{
                answer += String.valueOf(c) + "x^" + String.valueOf(b);
            }
        }

        return answer;
    }

    public String integral(Double[] a){

        int b = a.length;

        String answer = "";
        for(double x : a){
            double c = x/b;
            if(b>1) {
                answer += String.valueOf(c) + "x^" + String.valueOf(b) + " + ";
            }
            else{
                answer += String.valueOf(c) + "x^" + String.valueOf(b);
            }
            b-=1;
        }

        return answer;
    }




}
