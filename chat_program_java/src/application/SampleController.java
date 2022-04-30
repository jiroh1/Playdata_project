package application;

import java.util.List;

import Entity.EmpEntity;
import biz.EmpBiz;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import myjdbc.JDBCTemplate;
import dao.*;

public class SampleController {
public static JDBCTemplate db;

@FXML
public TextField Main_id;

@FXML
public TextField main_pass;

@FXML
public Button MAIN_JOIN;

@FXML    
public void w_join(ActionEvent Action) {//버튼의 액션을 적는다.
	
		EmpBiz biz = new EmpBiz();
		String action = "";
		
		// select
		List<EmpEntity> entity;// = new ArrayList<EmpEntity>(); 
		entity = biz.getSelectAll();
//			 
//		System.out.println(entity);	 
//		for (EmpEntity r : entity)	 {
//			 System.out.println(1);
//			 System.out.println(r.getId());
//			 System.out.println(r.getPw());
//		}
		
		entity = biz.getSelectAll();
		for (EmpEntity r : entity) {
			String i  = r.getId();
			String p = r.getPw();
			if (i.equals(Main_id.getText()) && p.equals(main_pass.getText())) {
				System.out.println("로그인 성공했습니다");
				Alert alert = new Alert(AlertType.INFORMATION);
				alert.setContentText("로그인성공이지롱!!!!");
				alert.show();
				action = "로그인 성공!";
				try{
			    	Parent Login = FXMLLoader.load(getClass().getResource("Window.fxml"));
				    Scene scene = new Scene(Login);
				    Stage primaryStage = (Stage)MAIN_JOIN.getScene().getWindow(); 
				    primaryStage.setScene(scene);
				    
				     }catch(Exception e){
				       e.printStackTrace();
				       }
				
//			}else if(Main_id.equals(Main_id) || main_pass.equals(main_pass)) {
//				System.out.println("로그인 실패ㅡㅡ");
//				Alert alert = new Alert(AlertType.INFORMATION);
//				alert.setContentText("로그인실패지롱!!!!");
//				alert.show();
//				Main_id.clear();
//				main_pass.clear();
//				Main_id.requestFocus();				
			} else {
				Alert alert = new Alert(AlertType.INFORMATION);
	            alert.setContentText("로그인 실패!! 아이디 혹은 비밀번호가 맞지 않습니다!!");
	            alert.show();
	            Main_id.clear();
	            main_pass.clear();
	            Main_id.requestFocus();
			}
		}	
}
//		 for (int i =0; i< entity.size();i++) {
//				if(!this.getPw.equals(sign_pass.getText())) {
//					check = 0;
//					break;
//				}
//				else if( this.id != null && total_info.get(i).getUser_id().equals(this.id)) {
//					check=1;
//					break;
//				}
//				else if( this.email != null && total_info.get(i).getUser_email().equals(this.email)) {
//					check=2;
//					break;
//				}
//				else if(this.tel != null && total_info.get(i).getUser_tel().equals(this.tel)) {
//					check=3;
//					break;
//				}
//				else {
//					check=4;
//				}
//			}		 

	
//	try{
//    	Parent Login = FXMLLoader.load(getClass().getResource("Window.fxml"));
//	    Scene scene = new Scene(Login);
//	    Stage primaryStage = (Stage)MAIN_JOIN.getScene().getWindow(); 
//	    primaryStage.setScene(scene);
//	    
//	     }catch(Exception e){
//	       e.printStackTrace();
//	       }
	 
@FXML    
public void signIn(ActionEvent Action) {//버튼의 액션을 적는다.
	try{
    	Parent Login = FXMLLoader.load(getClass().getResource("sign_id.fxml"));
	    Scene scene = new Scene(Login);
	    Stage primaryStage = (Stage)MAIN_CREATE.getScene().getWindow(); 
	    primaryStage.setScene(scene);
	    primaryStage.show();
	     }catch(Exception e){
	       e.printStackTrace();
	       }}	

@FXML
public Button MAIN_CANCEL;

@FXML
public Button MAIN_CREATE;
}
