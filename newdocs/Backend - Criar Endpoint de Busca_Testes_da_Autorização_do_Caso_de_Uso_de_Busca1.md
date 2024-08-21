```csharp
namespace Project.Tests.Application.UseCases.Brands.GetAllBrands.Behaviors
{
    public class GetAllBrandsAuthorizationBehaviorTest
    {
        private readonly IAuthorizationService _authorizationService = Substitute.For<IAuthorizationService>();
        private readonly RequestHandlerDelegate<PaginatedResponse<GetAllBrandsDto>> _requestHandler = Substitute.For<RequestHandlerDelegate<PaginatedResponse<GetAllBrandsDto>>>();

        [Fact]
        public async Task ThrowException_UserNotFound()
        {
            var handler = new GetAllBrandsAuthorizationBehavior(_authorizationService);

            var ex = await Assert.ThrowsAsync<UnauthorizedAccessException>(
                () => handler.Handle(BrandHelper.RandomGetAllBrandsQuery(), _requestHandler));

            Assert.Equal("User has no authorization to execute this request!", ex.Message);
        }

        [Fact]
        public async Task Handle_CallsNext_WhenUserIsAuthorized()
        {
            // Arrange
            var handler = new GetAllBrandsAuthorizationBehavior(_authorizationService);
            var query = BrandHelper.RandomGetAllBrandsQuery();
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