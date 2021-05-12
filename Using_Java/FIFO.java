import java.util.Arrays;
import java.util.Scanner;

public class FIFO {
    static Scanner sc = new Scanner(System.in);
    static FIFO obj = new FIFO();
    String[] process_input(){
        System.out.println("Enter pages (comma separated):");
        String input_string = sc.nextLine();
        return input_string.split(",");
    }

    String[] remove_element(String [] arr, int index){
        String[] new_arr = new String[arr.length-1];
        int i=0, count=0;
        for (i=0; i< arr.length; i++)
            if (index == i)
                new_arr[count] = arr[i];
        return new_arr;
    }


    public static void main(String[] args) {
        String[] pages = obj.process_input();
        String[] current_list = new String[pages.length * 10];
        String flag = "miss";
        int miss_count=0, hit_count = 0, count=0;
        System.out.print("Enter Frame length:");
        int frame_length = sc.nextInt();
        int current_list_counter = 0;
        for (String i : pages){
            if (!Arrays.asList(current_list).contains(i)){
                if (current_list_counter == frame_length) {
                    obj.remove_element(current_list, 0); // doing same thing as current_list.pop(0)
                    current_list_counter--;
                }
                current_list[current_list_counter++] = i;
                miss_count ++;
                flag = "miss";
            }
            else{
                hit_count ++;
                flag = "hit";
            }
            count ++;
            String[] temp_list = current_list;
            // TODO: proceed from here
        }
    }
}
