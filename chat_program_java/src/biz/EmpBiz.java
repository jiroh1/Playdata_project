package biz;

import java.sql.Connection;
import java.util.List;
import Entity.EmpEntity;
import dao.EmpDao;

import static myjdbc.JDBCTemplate.*; //import static�� �ָ� .�ϸ� class + �޼��尡 �ö�´�. 

// controller �� ���� ��ȿ�� ������ ������ vo�� �޾� ������ �Ÿ� ���� Ŭ������ ȣ���� ����� �����ϰ�
// �Ǵ� �ٷ� ������� ������ ���̽��� �����Ϸ��� dao�� �θ���. 
// JDBCTemplate�� �̿��ؼ� C&C�� ȣ���Ѵ�. 

public class EmpBiz {

	public List<EmpEntity> getSelectAll(){
		// ���� �ڵ带 ȣ���ؼ� ������ ���̽� ���� ...
		// vo�� �޾Ƽ� ���� Ŭ������ �� ���� entity�� ��Ƽ� dao�� �Ѱܼ� ���Ϲ޴´�
		Connection con = getConnection();
		List<EmpEntity> res = new EmpDao(con).getselectAll();// biz���� dao�� �θ� , �����ڸ� ���� �Ѱ��ش� �׷� dao�ΰ�����
		Close(con);
		return res;
	}
	public int getEmpInsert(EmpEntity entity) {
		Connection con = getConnection();
		int res = new EmpDao(con).getEmpInsert(entity);
		Close(con);
		return res;
		}

	
	// update, delete �ʿ���� 	
//	public int getEmpUpdate(EmpEntity entity) {
//		Connection con = getConnection();
//		int res = new EmpDao(con).getEmpUpdate(entity);
//		Close(con);
//		return res;
//		}
//	
//	public int getEmpDelete(EmpEntity entity) {
//		Connection con = getConnection();
//		int res = new EmpDao(con).getEmpDelete(entity);
//		Close(con);
//		return res;
//		}
	
	}
	
