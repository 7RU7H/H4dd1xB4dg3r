use httpmock::Method::GET;

#[test]
fn handle_x() {
    assert_eq!();
}



    let server = MockServer::start();

    let mock = server.mock(|when, then| {
        when.method(GET).path("/");
        then.status(200).body("Test request");

