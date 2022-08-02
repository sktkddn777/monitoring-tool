user: root -> root 권한 부여
cadvisor : mac에서는 이슈가 좀 있다... amd64 뭐시기..
그래서 ec2에서 직접 테스트 진행 하였는데, 공식 이미지로 성공했다.

1. node exporter 실행
2. cadvisor 실행
3. prometheus 실행
4. grafana 실행
5. slack alert done
