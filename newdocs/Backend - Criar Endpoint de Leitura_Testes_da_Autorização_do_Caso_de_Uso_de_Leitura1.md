```csharp
namespace Project.Tests.Application.UseCases.Brands.GetBrandById.Behaviors
{
    public class GetBrandByIdAuthorizationBehaviorTest
    {
        private readonly IAuthorizationService _authorizationService = Substitute.For<IAuthorizationService>();
        private readonly RequestHandlerDelegate<GetBrandByIdDto> _requestHandler = Substitute.For<RequestHandlerDelegate<GetBrandByIdDto>>();

        [Fact]
        public async Task ThrowException_UserNotFound()
        {
            var handler = new GetBrandByIdAuthorizationBehavior(_authorizationService);

            var ex = await Assert.ThrowsAsync<UnauthorizedAccessException>(
                () => handler.Handle(BrandHelper.RandomGetBrandByIdQuery(), _requestHandler));

            Assert.Equal("User has no authorization to execute this request!", ex.Message);
        }

        [Fact]
        public async Task Handle_CallsNext_WhenUserIsAuthorized()
        {
            // Arrange
            var handler = new GetBrandByIdAuthorizationBehavior(_authorizationService);
            var query = BrandHelper.RandomGetBrandByIdQuery();
            var user = new User(); // Assuming a User class exists

            _authorizationService.GetUserAsync().Returns(user);

            // Act
            await handler.Handle(query, _requestHandler);

            // Assert
            await _requestHandler.Received(1)();
        }
    }
}
```