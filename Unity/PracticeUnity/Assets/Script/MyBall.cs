using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MyBall : MonoBehaviour
{
    Rigidbody rigid;    
    void Start()
    {
        rigid = GetComponent<Rigidbody>();
       
    }

   
    void FixedUpdate()
    {
        // rigid.velocity = Vector3.forward;
        if (Input.GetButtonUp("Jump")){
            rigid.AddForce(Vector3.up * 5, ForceMode.Impulse);
            Debug.Log(rigid.velocity);
        }

        Vector3 vec = new Vector3(Input.GetAxisRaw("Horizontal"), 0, Input.GetAxisRaw("Vertical"));

        rigid.AddForce(vec, ForceMode.Impulse);
    }
}
