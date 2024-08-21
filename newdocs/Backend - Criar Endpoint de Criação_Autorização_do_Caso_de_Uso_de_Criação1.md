```csharp
namespace Project.Application.UseCases.Brands.CreateBrand.Behaviors
{
    public class CreateBrandAuthorizationBehavior : IPipelineBehavior<CreateBrandCommand, CreateBrandDto>
    {
        private readonly IAuthorizationService _authorizationService;

        public CreateBrandAuthorizationBehavior(IAuthorizationService authorizationService)
        {
            _authorizationService = authorizationService;
        }

        public async Task<CreateBrandDto> Handle(CreateBrandCommand command, RequestHandlerDelegate<CreateBrandDto> next, CancellationToken ct = default)
        {
            var user = await _authorizationService.GetUserAsync() ??
                throw new UnauthorizedAccessException("User has no authorization to execute this request!");

            return await next();
        }
    }
}
```