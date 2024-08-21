```csharp
namespace Project.Tests.Application.UseCases.Brands.DeleteBrand.Behaviors
{
    public class DeleteBrandAuthorizationBehaviorTest
    {
        private readonly IAuthorizationService _authorizationService = Substitute.For<IAuthorizationService>();
        private readonly RequestHandlerDelegate<Unit> _requestHandler = Substitute.For<RequestHandlerDelegate<Unit>>();

        [Fact]
        public async Task ThrowException_UserNotFound()
        {
            var handler = new DeleteBrandAuthorizationBehavior(_authorizationService);

            var ex = await Assert.ThrowsAsync<UnauthorizedAccessException>(
                () => handler.Handle(BrandHelper.RandomDeleteBrandCommand(), _requestHandler));

            Assert.Equal("User has no authorization to execute this request!", ex.Message);
        }

        [Fact]
        public async Task Handle_CallsNext_WhenUserIsAuthorized()
        {
            // Arrange
            var handler = new DeleteBrandAuthorizationBehavior(_authorizationService);
            var command = BrandHelper.RandomDeleteBrandCommand();
            var user = new User(); // Assuming a User class exists

            _authorizationService.GetUserAsync().Returns(user);

            // Act
            await handler.Handle(command, _requestHandler);

            // Assert
            await _requestHandler.Received(1)();
        }
    }
}
```