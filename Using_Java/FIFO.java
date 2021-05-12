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

    String[] reverse(String[] arr){
        String temp;
        int n = arr.length, k= n-1;
        for (int i=0;i<(n/2);i++)
        {
            temp = arr[i];
            arr[i] = arr[k];
            arr[k] = temp;
            k--;

        }
        return arr;
    }

    String[] remove_element(String[] arr){
        String[] new_arr = new String[arr.length];
        int i=0, count=0;
        for (i=0; i< arr.length; i++)
            if (0 == i)
                new_arr[count] = arr[i];
        return new_arr;
    }

    String join(String[] arr, String joiner){
        StringBuilder arr_rep = new StringBuilder();
        int length = arr.length, count=0;
        for (String ch : arr){
            if (count != 0)
                arr_rep.append(joiner).append(ch);
            else
                arr_rep.append(ch);
            count ++;
        }
        return arr_rep.toString();
    }


    public static void main(String[] args) {
        String demo = """
You Can Either enter string like this:
    1,3,0,3,5,6
        or,
    You can Also Enter like this:
        130356
(for better readability the first method is recommended,

However--> For quick and easy entry you can also use the 2nd method of input)
        --- in both the cases you get the same output ---
""";
        System.out.println(demo);

        String[] pages = obj.process_input();
        String flag = "miss";
        int miss_count=0, hit_count = 0, count=0;
        System.out.print("Enter Frame length:");
        int frame_length = sc.nextInt();
        String[] current_list = new String[frame_length];
        int current_list_counter = 0;
        for (String i : pages){
            if (!Arrays.asList(current_list).contains(i)){
                if (current_list_counter == frame_length) {
                    current_list = obj.remove_element(current_list); // doing same thing as current_list.pop(0)
                    --current_list_counter;
                }
                current_list[current_list_counter] = i;
                current_list_counter ++;
                miss_count ++;
                flag = "miss";
            }
            else{
                hit_count ++;
                flag = "hit";
            }
            count ++;
            String[] temp_list = current_list;
            temp_list = obj.reverse(temp_list);
            System.out.printf(">>%s %d with:(%s)%s%s%s","step", count, i, ".\n|",
                    obj.join(temp_list, "|\n|"), "|");
            System.out.println("\t" + flag + "\n");
        }

        int miss_percent = (miss_count / pages.length) * 100;
        int hit_percent = (hit_count / pages.length) * 100;
        System.out.printf("\nMiss count:%d, Hit count:%d\n________________\n",miss_count, hit_count);
        System.out.printf("The miss percent is: %d and\nthe hit percent is: %d", miss_percent, hit_percent);
    }
}
