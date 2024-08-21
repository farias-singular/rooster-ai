```csharp
namespace Project.Tests.Application.UseCases.Brands.CreateBrand.Behaviors
{
    public class CreateBrandAuthorizationBehaviorTest
    {
        private readonly IAuthorizationService _authorizationService = Substitute.For<IAuthorizationService>();
        private readonly RequestHandlerDelegate<CreateBrandDto> _requestHandler = Substitute.For<RequestHandlerDelegate<CreateBrandDto>>();

        [Fact]
        public async Task ThrowException_UserNotFound()
        {
            var handler = new CreateBrandAuthorizationBehavior(_authorizationService);

            var ex = await Assert.ThrowsAsync<UnauthorizedAccessException>(
                () => handler.Handle(BrandHelper.RandomCreateBrandCommand(), _requestHandler));

            Assert.Equal("User has no authorization to execute this request!", ex.Message);
        }

        [Fact]
        public async Task Handle_CallsNext_WhenUserIsAuthorized()
        {
            // Arrange
            var handler = new CreateBrandAuthorizationBehavior(_authorizationService);
            var command = BrandHelper.RandomCreateBrandCommand();
            var user = EntityFaker.RandomUser(type: UserType.Admin);

            _authorizationService.GetUserAsync().Returns(user);

            // Act
            await handler.Handle(command, _requestHandler);

            // Assert
            await _requestHandler.Received(1)();
        }
    }
}
```